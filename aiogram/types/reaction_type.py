import typing

from . import base
from . import fields
from ..utils import helper
from ..utils.helper import Item


class ReactionType(base.TelegramObject):
	"""
	This object describes the type of a reaction. Currently, it can be one of

	 - ReactionTypeEmoji
	 - ReactionTypeCustomEmoji
	"""
	type: base.String = fields.Field()

	@classmethod
	def resolve(cls, **kwargs) -> typing.Union[
		"ReactionTypeEmoji",
		"ReactionTypeCustomEmoji",
	]:
		type_ = kwargs.get('type')
		mapping = {
			ReactionTypeType.EMOJI: ReactionTypeEmoji,
			ReactionTypeType.CUSTOM_EMOJI: ReactionTypeCustomEmoji,
		}
		class_ = mapping.get(type_)
		if not class_:
			raise ValueError(f'Unknown ReactionType type: {type_}')
		return class_(**kwargs)


class ReactionTypeEmoji(ReactionType):
	"""
	The reaction is based on an emoji.

	Source: https://core.telegram.org/bots/api#reactiontypeemoji
	"""
	type: base.String = fields.Field(default='emoji')
	emoji: base.String = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='emoji', **kwargs)


class ReactionTypeCustomEmoji(ReactionType):
	"""
	The reaction is based on a custom emoji.

	Source: https://core.telegram.org/bots/api#reactiontypeemoji
	"""
	type: base.String = fields.Field(default='custom_emoji')
	custom_emoji_id: base.String = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='custom_emoji', **kwargs)


class ReactionTypeType(helper.Helper):
	mode = helper.HelperMode.lowercase

	EMOJI = Item()
	CUSTOM_EMOJI = Item()
