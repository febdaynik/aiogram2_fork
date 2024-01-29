from . import base
from . import fields
from .chat import Chat
from .maybe_inaccessible_message import MaybeInaccessibleMessage


class InaccessibleMessage(MaybeInaccessibleMessage):
	"""
	This object describes a message that was deleted or is otherwise inaccessible to the bot.

	Source: https://core.telegram.org/bots/api#inaccessiblemessage
	"""

	chat: Chat = fields.Field(base=Chat)
	message_id: base.Integer = fields.Field()
	date: base.Integer = fields.Field()
