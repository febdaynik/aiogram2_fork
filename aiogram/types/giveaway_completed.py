from typing import TYPE_CHECKING

from . import base, fields
if TYPE_CHECKING:
	from .message import Message


class GiveawayCompleted(base.TelegramObject):
	"""
	This object represents a service message about the completion of a giveaway without public winners.

	Source: https://core.telegram.org/bots/api#giveawaycompleted
	"""

	winner_count: base.Integer = fields.Field()
	unclaimed_prize_count: base.Integer = fields.Field()
	giveaway_message: 'Message' = fields.Field(base='Message')
