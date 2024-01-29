from . import base
from . import fields
from .chat import Chat
from .chat_boost import ChatBoost


class ChatBoostUpdated(base.TelegramObject):
	"""
	This object represents a boost added to a chat or changed.

	Source: https://core.telegram.org/bots/api#chatboostupdated
	"""

	chat: Chat = fields.Field(base=Chat)
	boost: ChatBoost = fields.Field(base=ChatBoost)
