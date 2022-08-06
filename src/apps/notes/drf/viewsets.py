from core.drf.permissions import IsOwner
from core.drf.viewsets import ModelOwnerViewSet

from ..models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelOwnerViewSet):
    permission_classes = (IsOwner,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
