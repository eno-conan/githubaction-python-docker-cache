from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
import datetime
from loguru import logger
import sys
# from starlette.routing import Match

logger.remove()
logger.add(sys.stdout, colorize=True, format="{time:HH:mm:ss} | {level} | {message}")


class LoguruRouteLogging(BaseHTTPMiddleware):
    """各ルートの実行内容をログ出力
    API内で各エンドポイントにアクセスした際に、アクセス内容をログに残す
    Args:
        BaseHTTPMiddleware :
        リクエスト/レスポンスインタフェースに対するASGIミドルウェアを記述するための抽象クラス.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        before = time.time()
        record = {}
        time_local = datetime.datetime.fromtimestamp(
            before, tz=datetime.timezone(datetime.timedelta(hours=9))
        )
        # record["time_local"] = time_local.strftime("%Y/%m/%d %H:%M:%S%Z")
        logger.debug(time_local.strftime("%Y/%m/%d %H:%M:%S%Z"))
        logger.debug(f"{request.method} {request.url}")
        # routes params
        # routes = request.app.router.routes
        # logger.debug("Params:")
        # for route in routes:
        #     match, scope = route.matches(request)
        #     if match == Match.FULL:
        #         for name, value in scope["path_params"].items():
        #             logger.debug(f"\t{name}: {value}")
        # logger.debug("Headers:")
        # for name, value in request.headers.items():
        #     logger.debug(f"\t{name}: {value}")
        if await request.body():
            record["request_body"] = (await request.body()).decode("utf-8")
        response = await call_next(request)
        return response
