from config import celery_app

from .models import User


@celery_app.task()
def task_send_email():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()
