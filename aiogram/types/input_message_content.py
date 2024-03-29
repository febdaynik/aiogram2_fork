import typing

from . import base
from . import fields
from .message_entity import MessageEntity
from .labeled_price import LabeledPrice
from .link_preview_options import LinkPreviewOptions
from ..utils.payload import generate_payload


class InputMessageContent(base.TelegramObject):
    """
    This object represents the content of a message to be sent as a result of an inline query.

    Telegram clients currently support the following 4 types

    https://core.telegram.org/bots/api#inputmessagecontent
    """
    pass


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    phone_number: base.String = fields.Field()
    first_name: base.String = fields.Field()
    last_name: typing.Optional[base.String] = fields.Field()
    vcard: typing.Optional[base.String] = fields.Field()

    def __init__(self,
                 phone_number: base.String,
                 first_name: base.String = None,
                 last_name: typing.Optional[base.String] = None,
                 vcard: typing.Optional[base.String] = None,
                 ):
        super().__init__(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard
        )


class InputInvoiceMessageContent(InputMessageContent):
    """
    Represents the content of an invoice message to be sent as the
    result of an inline query.

    https://core.telegram.org/bots/api#inputinvoicemessagecontent
    """

    title: base.String = fields.Field()
    description: base.String = fields.Field()
    payload: base.String = fields.Field()
    provider_token: base.String = fields.Field()
    currency: base.String = fields.Field()
    prices: typing.List[LabeledPrice] = fields.ListField(base=LabeledPrice)
    max_tip_amount: typing.Optional[base.Integer] = fields.Field()
    suggested_tip_amounts: typing.Optional[
        typing.List[base.Integer]
    ] = fields.ListField(base=base.Integer)
    provider_data: typing.Optional[base.String] = fields.Field()
    photo_url: typing.Optional[base.String] = fields.Field()
    photo_size: typing.Optional[base.Integer] = fields.Field()
    photo_width: typing.Optional[base.Integer] = fields.Field()
    photo_height: typing.Optional[base.Integer] = fields.Field()
    need_name: typing.Optional[base.Boolean] = fields.Field()
    need_phone_number: typing.Optional[base.Boolean] = fields.Field()
    need_email: typing.Optional[base.Boolean] = fields.Field()
    need_shipping_address: typing.Optional[base.Boolean] = fields.Field()
    send_phone_number_to_provider: typing.Optional[base.Boolean] = fields.Field()
    send_email_to_provider: typing.Optional[base.Boolean] = fields.Field()
    is_flexible: typing.Optional[base.Boolean] = fields.Field()

    def __init__(
        self,
        title: base.String,
        description: base.String,
        payload: base.String,
        provider_token: base.String,
        currency: base.String,
        prices: typing.List[LabeledPrice] = None,
        max_tip_amount: typing.Optional[base.Integer] = None,
        suggested_tip_amounts: typing.Optional[typing.List[base.Integer]] = None,
        provider_data: typing.Optional[base.String] = None,
        photo_url: typing.Optional[base.String] = None,
        photo_size: typing.Optional[base.Integer] = None,
        photo_width: typing.Optional[base.Integer] = None,
        photo_height: typing.Optional[base.Integer] = None,
        need_name: typing.Optional[base.Boolean] = None,
        need_phone_number: typing.Optional[base.Boolean] = None,
        need_email: typing.Optional[base.Boolean] = None,
        need_shipping_address: typing.Optional[base.Boolean] = None,
        send_phone_number_to_provider: typing.Optional[base.Boolean] = None,
        send_email_to_provider: typing.Optional[base.Boolean] = None,
        is_flexible: typing.Optional[base.Boolean] = None,
    ):
        if prices is None:
            prices = []
        payload = generate_payload(**locals())
        super().__init__(**payload)


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    latitude: base.Float = fields.Field()
    longitude: base.Float = fields.Field()
    horizontal_accuracy: typing.Optional[base.Float] = fields.Field()
    live_period: typing.Optional[base.Integer] = fields.Field()
    heading: typing.Optional[base.Integer] = fields.Field()
    proximity_alert_radius: typing.Optional[base.Integer] = fields.Field()

    def __init__(self,
                 latitude: base.Float,
                 longitude: base.Float,
                 horizontal_accuracy: typing.Optional[base.Float] = None,
                 live_period: typing.Optional[base.Integer] = None,
                 heading: typing.Optional[base.Integer] = None,
                 proximity_alert_radius: typing.Optional[base.Integer] = None,
                 ):
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
        )


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    message_text: base.String = fields.Field()
    parse_mode: typing.Optional[base.String] = fields.Field()
    entities: typing.Optional[typing.List[MessageEntity]] = fields.Field()
    link_preview_options: typing.Optional[LinkPreviewOptions] = fields.Field(base=LinkPreviewOptions)

    def safe_get_parse_mode(self):
        try:
            return self.bot.parse_mode
        except RuntimeError:
            pass

    def safe_get_link_preview_options(self):
        try:
            return self.bot.link_preview_options
        except RuntimeError:
            pass

    def __init__(
            self,
            message_text: base.String,
            parse_mode: typing.Optional[base.String] = None,
            entities: typing.Optional[typing.List[MessageEntity]] = None,
            link_preview_options: typing.Optional[LinkPreviewOptions] = None,
    ):
        if parse_mode is None:
            parse_mode = self.safe_get_parse_mode()
        if link_preview_options is None:
            link_preview_options = self.safe_get_link_preview_options()

        super().__init__(
            message_text=message_text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
        )


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    latitude: base.Float = fields.Field()
    longitude: base.Float = fields.Field()
    title: base.String = fields.Field()
    address: base.String = fields.Field()
    foursquare_id: typing.Optional[base.String] = fields.Field()
    foursquare_type: typing.Optional[base.String] = fields.Field()
    google_place_id: typing.Optional[base.String] = fields.Field()
    google_place_type: typing.Optional[base.String] = fields.Field()

    def __init__(
            self,
            latitude: base.Float,
            longitude: base.Float,
            title: base.String,
            address: base.String,
            foursquare_id: typing.Optional[base.String] = None,
            foursquare_type: typing.Optional[base.String] = None,
            google_place_id: typing.Optional[base.String] = None,
            google_place_type: typing.Optional[base.String] = None,
    ):
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
        )
