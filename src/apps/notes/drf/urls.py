from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .viewsets import NoteViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", NoteViewSet, basename="notes")

urlpatterns = router.urls
