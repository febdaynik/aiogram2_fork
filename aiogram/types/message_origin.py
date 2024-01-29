import typing

from . import base
from . import fields
from .chat import Chat
from .user import User
from ..utils import helper
from ..utils.helper import Item


class MessageOrigin(base.TelegramObject):
	"""
	This object describes the origin of a message. It can be one of

	- MessageOriginUser
	- MessageOriginHiddenUser
	- MessageOriginChat
	- MessageOriginChannel
	"""

	type: base.String = fields.Field()
	date: base.Integer = fields.Field()

	@classmethod
	def resolve(cls, **kwargs) -> typing.Union[
		"MessageOriginUser",
		"MessageOriginHiddenUser",
		"MessageOriginChat",
		"MessageOriginChannel",
	]:
		type_ = kwargs.get('type')
		mapping = {
			MessageOriginType.USER: MessageOriginUser,
			MessageOriginType.HIDDEN_USER: MessageOriginHiddenUser,
			MessageOriginType.CHAT: MessageOriginChat,
			MessageOriginType.CHANNEL: MessageOriginChannel,
		}
		class_ = mapping.get(type_)
		if not class_:
			raise ValueError(f'Unknown MessageOrigin type: {type_}')
		return class_(**kwargs)


class MessageOriginUser(MessageOrigin):
	"""
	The message was originally sent by a known user.

	Source: https://core.telegram.org/bots/api#messageoriginuser
	"""
	type: base.String = fields.Field(default='user')
	date: base.Integer = fields.Field()
	sender_user: User = fields.Field(base=User)

	def __init__(self, **kwargs):
		super().__init__(type='user', **kwargs)


class MessageOriginHiddenUser(MessageOrigin):
	"""
	The message was originally sent by an unknown user.

	Source: https://core.telegram.org/bots/api#messageoriginhiddenuser
	"""
	type: base.String = fields.Field(default='hidden_user')
	date: base.Integer = fields.Field()
	sender_user_name: base.String = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='hidden_user', **kwargs)


class MessageOriginChat(MessageOrigin):
	"""
	The message was originally sent on behalf of a chat to a group chat.

	Source: https://core.telegram.org/bots/api#messageoriginchat
	"""
	type: base.String = fields.Field(default='chat')
	date: base.Integer = fields.Field()
	sender_chat: Chat = fields.Field(base=Chat)
	author_signature: base.String = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='chat', **kwargs)


class MessageOriginChannel(MessageOrigin):
	"""
	The message was originally sent to a channel chat.

	Source: https://core.telegram.org/bots/api#messageoriginchannel
	"""
	type: base.String = fields.Field(default='chat')
	date: base.Integer = fields.Field()
	chat: Chat = fields.Field(base=Chat)
	message_id: base.Integer = fields.Field()
	author_signature: base.String = fields.Field()

	def __init__(self, **kwargs):
		super().__init__(type='chat', **kwargs)


class MessageOriginType(helper.Helper):
	mode = helper.HelperMode.lowercase

	USER = Item()
	HIDDEN_USER = Item()
	CHAT = Item()
	CHANNEL = Item()
