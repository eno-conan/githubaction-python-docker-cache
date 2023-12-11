import logging
import os
from typing import Any

from fastapi import FastAPI, status
from mangum import Mangum
from pydantic import BaseModel

from src.core.config import settings
from src.core.log_filters import EndpointFilter

from src.exceptions.error_handle_middleware import ErrorHandlingMiddleware
from src.core.logger.loguru_route_logging import LoguruRouteLogging

# "Receive Event" Annotation
EventAny = Any

# 環境によって設定制御
env = os.getenv("ENV")
if env is None:
    app = FastAPI(
        title=settings.title,
        version=settings.version,
    )
else:
    app = FastAPI(
        root_path="/dev",
        title=settings.title,
        version=settings.version,
    )
app.add_middleware(ErrorHandlingMiddleware)
app.add_middleware(LoguruRouteLogging)

# 除外したいエンドポイントを指定
excluded_endpoints = ["/favicon.ico"]
# フィルター追加
logging.getLogger("uvicorn.access").addFilter(EndpointFilter(excluded_endpoints))


class HealthCheck(BaseModel):

    """Response model to validate and return when performing a health check."""

    status: str = "OK"


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """Calculate speed as distance divided by time.

    Returns:
        status
    """
    return HealthCheck(status="OK")


def handler(event: EventAny, context: EventAny):
    asgi_handler = Mangum(app)
    return asgi_handler(event, context)
