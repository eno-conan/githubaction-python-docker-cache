from typing import Any

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.logger.api_logger import ApiLogger


# ref: https://qiita.com/sotaheavymetal21/items/508a458a70962d822cb5
class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """エラーハンドリングをするミドルウェア
    API内で発生したエラーをキャッチして処理を施す
    Args:
        BaseHTTPMiddleware :
        リクエスト/レスポンスインタフェースに対するASGIミドルウェアを記述するための抽象クラス.
    """

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        try:
            # 各エンドポイント内で発生したエラーに関しては
            # HttpExceptionをraise
            # FastAPI側でエラーハンドリングをしエラーレスポンスを返す想定
            response: Response = await call_next(request)

        # 現時点で観測できていないエラー用
        # 例えば、APIの実装で、定義していない変数をaを呼び出す処理を追加
        # "a" is not definedを発生させたときに、以下のexceptの処理が実行される仕組み
        except Exception as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error_code":
                        e.__class__.__name__,
                    "error_msg": "エラーが発生しました、\
                        システム管理者に問い合わせてください",
                },
            )
            ApiLogger.error(response, exec_info=True)

        return response
