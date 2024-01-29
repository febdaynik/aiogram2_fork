import typing

from . import base
from . import fields
from .chat import Chat


class Giveaway(base.TelegramObject):
	"""
	This object represents a message about a scheduled giveaway.

	Source: https://core.telegram.org/bots/api#giveaway
	"""

	chats: typing.List[Chat] = fields.ListField(base=Chat)
	winners_selection_date: base.Integer = fields.Field()
	winner_count: base.Integer = fields.Field()
	only_new_members: base.Boolean = fields.Field()
	has_public_winners: base.Boolean = fields.Field()
	prize_description: base.String = fields.Field()
	country_codes: typing.List[base.String] = fields.ListField(base=base.String)
	premium_subscription_month_count: base.Integer = fields.Field()
