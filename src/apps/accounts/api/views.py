from core.drf.serializers import ErrorResponseSerializer
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from dj_rest_auth.views import LoginView as DefaultLoginView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, parsers, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSlidingSerializer
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import (
    LoginResponseSerializer,
    TokenResponseSerializer,
    UserImagesSerializer,
)

User = get_user_model()


class TokenViewResponseBase(TokenViewBase):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        if not getattr(serializer, "user", None):
            setattr(serializer, "user", request.user)
        if not getattr(serializer, "token", None):
            setattr(serializer, "token", serializer.validated_data["token"])

        return Response(
            TokenResponseSerializer(serializer).data, status=status.HTTP_200_OK
        )


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        responses={200: TokenResponseSerializer(), 401: ErrorResponseSerializer()}
    ),
)
class TokenRefreshSlidingView(TokenViewBase):
    serializer_class = TokenRefreshSlidingSerializer


class LoginSerializer(DefaultLoginSerializer):
    username = None

    def validate_email(self, val):
        return val.lower()


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        responses={200: LoginResponseSerializer(), 401: ErrorResponseSerializer()}
    ),
)
class LoginView(DefaultLoginView):
    serializer_class = LoginSerializer


class UserImagesView(generics.UpdateAPIView):
    serializer_class = UserImagesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (parsers.MultiPartParser,)

    def get_object(self):
        return self.request.user
