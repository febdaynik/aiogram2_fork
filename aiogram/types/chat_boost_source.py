import typing

from . import base
from . import fields
from .user import User
from ..utils import helper
from ..utils.helper import Item


class ChatBoostSource(base.TelegramObject):
	"""
	This object describes the source of a chat boost. It can be one of

	- ChatBoostSourcePremium
	- ChatBoostSourceGiftCode
	- ChatBoostSourceGiveaway
	"""
	source: base.String = fields.Field()
	user: User = fields.Field(base=User)

	@classmethod
	def resolve(cls, **kwargs) -> typing.Union[
		"ChatBoostSourcePremium",
		"ChatBoostSourceGiftCode",
		"ChatBoostSourceGiveaway",
	]:
		type_ = kwargs.get('type')
		mapping = {
			ChatBoostType.PREMIUM: ChatBoostSourcePremium,
			ChatBoostType.GIF_CODE: ChatBoostSourceGiftCode,
			ChatBoostType.GIVEAWAY: ChatBoostSourceGiveaway,
		}
		class_ = mapping.get(type_)
		if not class_:
			raise ValueError(f'Unknown ReactionType type: {type_}')
		return class_(**kwargs)


class ChatBoostSourcePremium(ChatBoostSource):
	"""
	The boost was obtained by subscribing to Telegram Premium or by gifting a
	Telegram Premium subscription to another user.

	Source: https://core.telegram.org/bots/api#chatboostsourcepremium
	"""

	source: base.String = fields.Field(default='premium')
	user: User = fields.Field(base=User)

	def __init__(self, **kwargs):
		super().__init__(type='premium', **kwargs)


class ChatBoostSourceGiftCode(ChatBoostSource):
	"""
	The boost was obtained by the creation of Telegram Premium gift codes to boost a chat.
	Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

	Source: https://core.telegram.org/bots/api#chatboostsourcegiftcode
	"""

	source: base.String = fields.Field(default='gif_code')
	user: User = fields.Field(base=User)

	def __init__(self, **kwargs):
		super().__init__(type='gif_code', **kwargs)


class ChatBoostSourceGiveaway(ChatBoostSource):
	"""
	The boost was obtained by the creation of a Telegram Premium giveaway.
	This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

	Source: https://core.telegram.org/bots/api#chatboostsourcegiveaway
	"""

	source: base.String = fields.Field(default='giveaway')
	user: User = fields.Field(base=User)
	giveaway_message_id: base.Integer = fields.Field()
	is_unclaimed: base.Boolean = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='giveaway', **kwargs)


class ChatBoostType(helper.Helper):
	mode = helper.HelperMode.lowercase

	PREMIUM = Item()
	GIF_CODE = Item()
	GIVEAWAY = Item()
