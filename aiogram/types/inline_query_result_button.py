import typing

from . import base
from . import fields
from .web_app_info import WebAppInfo


class InlineQueryResultsButton(base.TelegramObject):
	"""
	This object represents a button to be shown above inline query results.
	You must use exactly one of the optional fields.

	https://core.telegram.org/bots/api#inlinequeryresultsbutton
	"""
	text: base.String = fields.Field()
	web_app: WebAppInfo = fields.Field(base=WebAppInfo)
	start_parameter: base.String = fields.Field()

	def __init__(self, text: base.String,
				 web_app: typing.Optional[WebAppInfo] = None,
				 start_parameter: typing.Optional[base.String] = None):
		super(InlineQueryResultsButton, self).__init__(
			text=text,
			web_app=web_app,
			start_parameter=start_parameter
		)
