import typing

from . import base
from . import fields
from .message_entity import MessageEntity


class TextQuote(base.TelegramObject):
	"""
	This object contains information about the quoted part of a message that is replied to by the given message.

	Source: https://core.telegram.org/bots/api#textquote
	"""

	text: base.String = fields.Field()
	entities: typing.List[MessageEntity] = fields.ListField(base=MessageEntity)
	position: base.Integer = fields.Field()
	is_manual: base.Boolean = fields.Field()



