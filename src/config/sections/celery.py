from .base import TIME_ZONE, USE_TZ, env
from .logging import DjangoLogHandler, LOGGING_APP_NAME

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL", None)
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


CELERY_LOGGING = env.str("CELERY_LOGGING", None)
# TODO: add a default celery logger class
CELERY_LOGGING_CLASS = env.str("CELERY_LOGGING_CLASS", None)

if CELERY_LOGGING:
    from celery.signals import after_setup_logger, after_setup_task_logger
    import logging as base_logging
    logger = base_logging.getLogger(LOGGING_APP_NAME)

    @after_setup_logger.connect
    @after_setup_task_logger.connect
    def setup_celery_logging(logger, **kwargs):
        celery_logger = DjangoLogHandler(
            CELERY_LOGGING_CLASS
        )
        celery_logger.attach_to(logger)