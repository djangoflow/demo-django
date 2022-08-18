from df_auth.djangoflow.settings import *
from df_notifications.djangoflow.settings import *

DF_APPS = list(set(DF_AUTH_APPS) | set(DF_NOTIFICATIONS_APPS))
