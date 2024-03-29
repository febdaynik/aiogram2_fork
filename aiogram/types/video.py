from . import base
from . import fields
from . import mixins
from .photo_size import PhotoSize


class Video(base.TelegramObject, mixins.Downloadable):
    """
    This object represents a video file.

    https://core.telegram.org/bots/api#video
    """
    file_id: base.String = fields.Field()
    file_unique_id: base.String = fields.Field()
    width: base.Integer = fields.Field()
    height: base.Integer = fields.Field()
    duration: base.Integer = fields.Field()
    thumbnail: PhotoSize = fields.Field(base=PhotoSize)
    file_name: base.String = fields.Field()
    mime_type: base.String = fields.Field()
    file_size: base.Integer = fields.Field()
