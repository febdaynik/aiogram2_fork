from . import base
from . import fields
from .chat import Chat
from .chat_boost_source import ChatBoostSource


class ChatBoostRemoved(base.TelegramObject):
	"""
	This object represents a boost removed from a chat.

	Source: https://core.telegram.org/bots/api#chatboostremoved
	"""

	chat: Chat = fields.Field(base=Chat)
	boost_id: base.String = fields.Field()
	remove_date: base.Integer = fields.Field()
	source: ChatBoostSource = fields.Field(base=ChatBoostSource)
