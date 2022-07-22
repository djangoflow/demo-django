from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from dj_rest_auth.views import LoginView as DefaultLoginView
from django.contrib.auth import get_user_model
from rest_framework import generics, parsers, permissions


from .serializers import (
    UserImagesSerializer,
)

User = get_user_model()


class LoginSerializer(DefaultLoginSerializer):
    username = None

    def validate_email(self, val):
        return val.lower()


class LoginView(DefaultLoginView):
    serializer_class = LoginSerializer


class UserImagesView(generics.UpdateAPIView):
    serializer_class = UserImagesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (parsers.MultiPartParser,)

    def get_object(self):
        return self.request.user
