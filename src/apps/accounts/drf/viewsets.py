from core.drf.permissions import IsOwner
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    authentication_classes = (IsOwner,)
    serializer_class = UserSerializer

    # TODO: refactor this for special '_' id
    def get_object(self):
        return self.request.user
