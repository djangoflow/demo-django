from rest_framework.viewsets import GenericViewSet

from core.drf.permissions import IsOwner


class UserViewSet(GenericViewSet):
    authentication_classes = (IsOwner,)

    # TODO: refactor this for special '_' id
    def get_object(self):
        return self.request.user
