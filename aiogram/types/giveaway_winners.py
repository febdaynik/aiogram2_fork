import typing

from . import base
from . import fields
from .chat import Chat
from .user import User


class GiveawayWinners(base.TelegramObject):
	"""
	This object represents a message about the completion of a giveaway with public winners.

	Source: https://core.telegram.org/bots/api#giveawaywinners
	"""

	chat: Chat = fields.Field(base=Chat)
	giveaway_message_id: base.Integer = fields.Field()
	winners_selection_date: base.Integer = fields.Field()
	winner_count: base.Integer = fields.Field()
	winners: typing.List[User] = fields.ListField(base=User)
	additional_chat_count: base.Integer = fields.Field()
	premium_subscription_month_count: base.Integer = fields.Field()
	unclaimed_prize_count: base.Integer = fields.Field()
	only_new_members: base.Boolean = fields.Field()
	was_refunded: base.Boolean = fields.Field()
	prize_description: base.String = fields.Field()
