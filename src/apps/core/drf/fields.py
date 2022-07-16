from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers


class ChoiceDisplayField(serializers.ChoiceField):
    def __init__(self, choices, **kwargs):
        super().__init__(choices=choices, **kwargs)
        self._reverse_choices = dict((v, k) for k, v in self._choices.items())

    def to_representation(self, obj):
        return obj if obj == "" and self.allow_blank else self._choices[obj]

    def to_internal_value(self, data):
        if data is None or (data == "" and self.allow_blank):
            return data
        try:
            return self._reverse_choices[data]
        except KeyError:
            raise exceptions.ValidationError(_("{} is not a valid choice".format(data)))


class ImageAbsoluteURLField(serializers.URLField):
    def to_representation(self, image):
        if image and image.url:
            request = self.context.get("request", None)
            if request is not None:
                return request.build_absolute_uri(image.url)
            return image.url

        return None
