from core.drf.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        read_only_fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "force_password_change",
            "avatar",
        )
        fields = read_only_fields + ("tel",)


class TokenResponseSerializer(serializers.Serializer):
    user = UserSerializer(required=True)
    token = serializers.CharField(required=True)


class LoginResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    user = UserSerializer()


class UserImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar",)
