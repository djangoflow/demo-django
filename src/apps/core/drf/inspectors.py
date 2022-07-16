from drf_yasg import openapi
from drf_yasg.inspectors import ChoiceFieldInspector, NotHandled

from .fields import ChoiceDisplayField


class ChoiceDisplayFieldInspector(ChoiceFieldInspector):
    def field_to_swagger_object(self, field, *args, **kwargs):
        if isinstance(field, ChoiceDisplayField):
            schema = super().field_to_swagger_object(field, *args, **kwargs)
            schema.type = openapi.TYPE_STRING
            return schema
        return NotHandled
