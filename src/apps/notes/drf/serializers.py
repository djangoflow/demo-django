from ..models import Note
from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)
    user = HashidSerializerCharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    class Meta:
        model = Note
        read_only_fields = (
            "id",
            "created",
            "modified",
            "user",
        )
        fields = read_only_fields + ("text",)
