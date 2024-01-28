import typing

from . import base
from . import fields
from .chat import Chat
from .reaction_count import ReactionCount


class MessageReactionCountUpdated(base.TelegramObject):
	"""
	This object represents reaction changes on a message with anonymous reactions.

	Source: https://core.telegram.org/bots/api#messagereactioncountupdated
	"""
	chat: Chat = fields.Field(base=Chat)
	message_id: base.Integer = fields.Field()
	date: base.Integer = fields.Field()
	reactions: typing.List[ReactionCount] = fields.Field(base=ReactionCount)

