import typing

from . import base
from . import fields
from .reaction_type import ReactionType


class ReactionCount(base.TelegramObject):
	"""
	Represents a reaction added to a message along with the number of times it was added.

	Source: https://core.telegram.org/bots/api#reactioncount
	"""
	type: ReactionType = fields.Field(base=ReactionType)
	total_count: base.Integer = fields.Field()