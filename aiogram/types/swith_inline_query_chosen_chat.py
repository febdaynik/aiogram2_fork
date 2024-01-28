import typing

from . import base
from . import fields


class SwitchInlineQueryChosenChat(base.TelegramObject):
	"""
	This object represents an inline button that switches the current user to inline mode in a chosen chat,
	with an optional default inline query

	https://core.telegram.org/bots/api#switchinlinequerychosenchat
	"""
	query: typing.Optional[base.String] = fields.Field()
	allow_user_chats: typing.Optional[base.Boolean] = fields.Field()
	allow_bot_chats: typing.Optional[base.Boolean] = fields.Field()
	allow_group_chats: typing.Optional[base.Boolean] = fields.Field()
	allow_channel_chats: typing.Optional[base.Boolean] = fields.Field()
