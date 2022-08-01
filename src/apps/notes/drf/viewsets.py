from core.drf.permissions import IsOwner
from rest_framework.viewsets import ModelViewSet

from ..models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    permission_classes = (IsOwner,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
