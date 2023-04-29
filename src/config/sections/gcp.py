from .base import env
from .logging import DjangoLogHandler, LOGGING_APP_NAME
from django.utils.module_loading import import_string


GCP_LOGGING = env.str("GCP_LOGGING", None)
GCP_LOGGING_CLASS = env.str(
    "GCP_LOGGING_CLASS", "google.cloud.logging.handlers.CloudLoggingHandler"
)
GCP_LOGGING_CLIENT = env.str("GCP_LOGGING_CLIENT", "google.cloud.logging.Client")

if GCP_LOGGING:
    import logging as base_logging
    logger = base_logging.getLogger(LOGGING_APP_NAME)

    gcp_handler = DjangoLogHandler(
        sink_type=GCP_LOGGING_CLASS,
        handler_kwargs={
            "client": import_string(GCP_LOGGING_CLIENT)(),
            "name": LOGGING_APP_NAME
        }
    )
    gcp_handler.attach_to(logger)
