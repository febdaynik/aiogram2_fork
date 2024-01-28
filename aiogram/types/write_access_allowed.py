import typing

from . import base
from . import fields


class WriteAccessAllowed(base.TelegramObject):
    """
    This object represents a service message about a user allowing a bot added to the attachment menu to write messages.
    Currently holds no information.

    https://core.telegram.org/bots/api#writeaccessallowed
    """

    web_app_name: typing.Optional[base.String] = fields.Field()
