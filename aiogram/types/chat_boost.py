from . import base
from . import fields
from .chat_boost_source import ChatBoostSource


class ChatBoost(base.TelegramObject):
	"""
	This object contains information about a chat boost.

	Source: https://core.telegram.org/bots/api#chatboost
	"""

	boost_id: base.Integer = fields.Field()
	add_date: base.Integer = fields.Field()
	expiration_date: base.Integer = fields.Field()
	source: ChatBoostSource = fields.Field(base=ChatBoostSource)
