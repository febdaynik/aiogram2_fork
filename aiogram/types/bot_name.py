from . import base
from . import fields


class BotName(base.TelegramObject):
    """
    This object represents the bot's name.

    https://core.telegram.org/bots/api#botname
    """
    name: base.String = fields.Field()

    def __init__(self, name: base.String):
        super(BotName, self).__init__(name=name)