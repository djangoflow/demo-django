from rest_framework import serializers

from .fields import ChoiceDisplayField


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    code = serializers.CharField(required=True)
    field = serializers.CharField(required=False)


class ErrorResponseSerializer(serializers.Serializer):
    errors = ErrorSerializer(many=True, required=True)


class EmptyResponseSerializer(serializers.Serializer):
    pass


class ApiDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()


class ModelSerializer(serializers.ModelSerializer):
    serializer_choice_field = ChoiceDisplayField
