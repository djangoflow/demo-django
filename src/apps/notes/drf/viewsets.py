from core.drf.permissions import IsOwner
from core.drf.viewsets import ModelOwnerViewSet
from .serializers import NoteSerializer
from ..models import Note


class NoteViewSet(ModelOwnerViewSet):
    permission_classes = (IsOwner,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
