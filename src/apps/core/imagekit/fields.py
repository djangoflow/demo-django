from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill, Transpose


class ResizedImageField(ProcessedImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("blank", True)
        kwargs.setdefault("null", True)
        super().__init__(
            *args,
            processors=[
                ResizeToFill(kwargs.pop("width"), kwargs.pop("height")),
                Transpose(Transpose.AUTO),
            ],
            format="JPEG",
            options={"quality": 60},
            **kwargs
        )


class AvatarImageField(ResizedImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, width=100, height=100, **kwargs)


class FullImageField(ResizedImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, width=800, height=500, **kwargs)
