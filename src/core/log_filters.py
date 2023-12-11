import logging


class EndpointFilter(logging.Filter):
    def __init__(self, excluded_endpoints: list[str]) -> None:  # noqa: ANN101
        self.excluded_endpoints = excluded_endpoints

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: ANN101
        """
        Filter関数
        record.argsには ('127.0.0.1:51632', 'GET', '/ping', '1.1', 200) .
        """
        return (
            record.args
            and len(record.args) >= 3
            and record.args[2] not in self.excluded_endpoints
        )
