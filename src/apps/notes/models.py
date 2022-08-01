from accounts.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Note(TimeStampedModel):
    user_attribute = "user"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, default="")
