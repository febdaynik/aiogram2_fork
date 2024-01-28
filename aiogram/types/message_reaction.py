import typing

from . import base
from . import fields
from .chat import Chat
from .user import User
from .reaction_type import ReactionType


class MessageReactionUpdated(base.TelegramObject):
	"""
	This object represents a change of a reaction on a message performed by a user.

	Source: https://core.telegram.org/bots/api#messagereactionupdated
	"""
	chat: Chat = fields.Field(base=Chat)
	message_id: base.Integer = fields.Field()
	from_user: User = fields.Field(alias="user", base=User)
	actor_chat: Chat = fields.Field(base=Chat)
	date: base.Integer = fields.Field()
	old_reaction: typing.List[ReactionType] = fields.Field(base=ReactionType)
	new_reaction: typing.List[ReactionType] = fields.Field(base=ReactionType)

