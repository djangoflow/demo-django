from core.drf.permissions import IsOwner
from rest_framework.viewsets import GenericViewSet


class UserViewSet(GenericViewSet):
    authentication_classes = (IsOwner,)

    # TODO: refactor this for special '_' id
    def get_object(self):
        return self.request.user
