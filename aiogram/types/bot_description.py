from . import base
from . import fields


class BotDescription(base.TelegramObject):
    """
    This object represents the bot's description.

    https://core.telegram.org/bots/api#botdescription
    """
    description: base.String = fields.Field()

    def __init__(self, description: base.String):
        super(BotDescription, self).__init__(description=description)
