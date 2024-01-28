from . import base
from . import fields


class BotShortDescription(base.TelegramObject):
    """
    This object represents the bot's short description.

    https://core.telegram.org/bots/api#botshortdescription
    """
    short_description: base.String = fields.Field()

    def __init__(self, short_description: base.String):
        super(BotShortDescription, self).__init__(short_description=short_description)
