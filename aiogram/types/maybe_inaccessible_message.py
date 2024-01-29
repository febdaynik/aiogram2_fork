from . import base


class MaybeInaccessibleMessage(base.TelegramObject):
	"""
	This object describes a message that can be inaccessible to the bot. It can be one of

	- Message
	- InaccessibleMessage

	Source: https://core.telegram.org/bots/api#maybeinaccessiblemessage
	"""