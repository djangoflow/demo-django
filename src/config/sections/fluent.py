from .base import env
from .logging import DjangoLogHandler, LOGGING_APP_NAME

FLUENT_LOGGING = env.str("FLUENT_LOGGING", None)
FLUENT_LOGGING_HOST = env.str("FLUENT_HOST", "127.0.0.1")
FLUENT_LOGGING_PORT = env.str("FLUENT_PORT", "24224")
FLUENT_LOGGING_CLASS = env.str(
    "FLUENT_LOGGING_CLASS",
    "fluent.asynchandler.FluentHandler"
)

if FLUENT_LOGGING:
    import logging as base_logging
    logger = base_logging.getLogger(LOGGING_APP_NAME)

    fluent_handler = DjangoLogHandler(
        sink_type=FLUENT_LOGGING_CLASS,
        handler_kwargs={
            "host": FLUENT_LOGGING_HOST,
            "port": FLUENT_LOGGING_PORT
        }
    )
    fluent_handler.attach_to(logger)
