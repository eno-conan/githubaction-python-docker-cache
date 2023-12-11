import logging
from typing import Any

from aws_lambda_powertools import Logger


class ApiLogger:
    logger: logging.Logger = None

    @classmethod
    def info(cls, object_or_message: Any) -> None:
        """Info method."""
        cls._get_logger().info(object_or_message)

    @classmethod
    def debug(cls, object_or_message: Any) -> None:
        """Debug method."""
        cls._get_logger().debug(object_or_message)

    @classmethod
    def warn(cls, object_or_message: Any) -> None:
        """Warn method."""
        cls._get_logger().warning(object_or_message)

    @classmethod
    def error(cls, object_or_message: Any, exec_info: bool = False) -> None:
        """Error method."""
        cls._get_logger().error(object_or_message, exc_info=exec_info)

    @classmethod
    def _get_logger(cls) -> logging.Logger:
        """Private Get Logger method."""
        cls.logger = Logger(level="INFO", service=__name__)
        # if cls.logger is None:
        #     if settings.ENV == "local":
        #         cls.logger = logging.getLogger("uvicorn")
        #         cls.logger.setLevel(logging.DEBUG)
        #         cls.logger.addHandler(logging.StreamHandler())
        #     else:
        #         cls.logger = Logger(level="INFO", service=__name__)

        return cls.logger
