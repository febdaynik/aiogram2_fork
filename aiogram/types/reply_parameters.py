import typing

from . import base
from . import fields
from .message_entity import MessageEntity


class ReplyParameters(base.TelegramObject):
	"""
	Describes reply parameters for the message that is being sent.

	Source: https://core.telegram.org/bots/api#replyparameters
	"""

	message_id: base.Integer = fields.Field()
	chat_id: typing.Union[base.Integer, base.String] = fields.Field()
	allow_sending_without_reply: base.Boolean = fields.Field()
	quote: base.String = fields.Field()
	quote_parse_mode: base.String = fields.Field()
	quote_entities: typing.List[MessageEntity] = fields.ListField()
	quote_position: base.Integer = fields.Field()
