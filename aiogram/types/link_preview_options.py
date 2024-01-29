import typing

from . import base
from . import fields


class LinkPreviewOptions(base.TelegramObject):
	"""
	Describes the options used for link preview generation.

	Source: https://core.telegram.org/bots/api#linkpreviewoptions
	"""
	is_disabled: base.Boolean = fields.Field()
	url: base.String = fields.Field()
	prefer_small_media: base.Boolean = fields.Field()
	prefer_large_media: base.Boolean = fields.Field()
	show_above_text: base.Boolean = fields.Field()

	def __init__(self,
				 is_disabled: typing.Optional[base.Boolean] = None,
				 url: typing.Optional[base.String] = None,
				 prefer_small_media: typing.Optional[base.Boolean] = None,
				 prefer_large_media: typing.Optional[base.Boolean] = None,
				 show_above_text: typing.Optional[base.Boolean] = None):
		super().__init__(self, is_disabled=is_disabled, url=url, prefer_small_media=prefer_small_media,
						 prefer_large_media=prefer_large_media, show_above_text=show_above_text)