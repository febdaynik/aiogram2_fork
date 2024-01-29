from . import base
from . import fields
from .chat_boost import ChatBoost


class UserChatBoosts(base.TelegramObject):
	"""
	This object represents a list of boosts added to a chat by a user.

	Source: https://core.telegram.org/bots/api#userchatboosts
	"""

	boosts: ChatBoost = fields.ListField(base=ChatBoost)
