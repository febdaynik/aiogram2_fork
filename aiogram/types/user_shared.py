import typing

from . import base, fields


class UsersShared(base.TelegramObject):
    """
    This object contains information about the users whose identifiers were
    shared with the bot using a KeyboardButtonRequestUsers button.

    https://core.telegram.org/bots/api#usersshared
    """
    request_id: base.Integer = fields.Field()
    user_ids: typing.List[base.Integer] = fields.Field()
