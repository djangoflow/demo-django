from .base import env
from django.utils.module_loading import import_string
import logging as base_logging


# Logging config
# ------------------------------------------------------------------------------
LOGGING_APP_NAME = env.str("LOGGING_APP_NAME", "demo-django")
DJANGO_LOG_LEVEL = env.str("DJANGO_LOG_LEVEL", "INFO")
DEFAULT_LOG_FORMAT = "%(levelname)s %(asctime)s %(module)s \
%(process)d %(thread)d %(message)s"


class DjangoLogHandler:
    def __init__(self, sink_type, **kwargs):
        _class = import_string(sink_type)
        self._handler = self._class(**kwargs.get("handler_kwargs", {}))

    def attach_to(self, logger):
        logger.addHandler(self._handler)


logger = base_logging.getLogger(LOGGING_APP_NAME)
logger.setLevel(DJANGO_LOG_LEVEL)

CONSOLE_LOGGING_HANDLER_CLASS = env.str(
    "STREAM_LOGGING_HANDLER_CLASS", "logging.StreamHandler"
)
console_handler = DjangoLogHandler(CONSOLE_LOGGING_HANDLER_CLASS)
console_handler.attach_to(logger)
