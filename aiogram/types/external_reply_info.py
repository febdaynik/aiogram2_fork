import typing

from . import base
from . import fields
from .chat import Chat
from .animation import Animation
from .audio import Audio
from .document import Document
from .photo_size import PhotoSize
from .sticker import Sticker
from .story import Story
from .video import Video
from .video_note import VideoNote
from .voice import Voice
from .contact import Contact
from .dice import Dice
from .game import Game
from .giveaway import Giveaway
from .giveaway_winners import GiveawayWinners
from .invoice import Invoice
from .location import Location
from .link_preview_options import LinkPreviewOptions
from .message_origin import MessageOrigin
from .poll import Poll
from .venue import Venue


class ExternalReplyInfo(base.TelegramObject):
	"""
	This object contains information about a message that is being replied to,
	which may come from another chat or forum topic.

	Source: https://core.telegram.org/bots/api#externalreplyinfo
	"""

	origin: MessageOrigin = fields.Field(base=MessageOrigin)
	chat: Chat = fields.Field(base=Chat)
	message_id: base.Integer = fields.Field()
	link_preview_options: LinkPreviewOptions = fields.Field(base=LinkPreviewOptions)
	animation: Animation = fields.Field(base=Animation)
	audio: Audio = fields.Field(base=Audio)
	document: Document = fields.Field(base=Document)
	photo: typing.List[PhotoSize] = fields.ListField(base=PhotoSize)
	sticker: Sticker = fields.Field(base=Sticker)
	story: Story = fields.Field(base=Story)
	video: Video = fields.Field(base=Video)
	video_note: VideoNote = fields.Field(base=VideoNote)
	voice: Voice = fields.Field(base=Voice)
	has_media_spoiler: base.Boolean = fields.Field()
	contact: Contact = fields.Field(base=Contact)
	dice: Dice = fields.Field(base=Dice)
	game: Game = fields.Field(base=Game)
	giveaway: Giveaway = fields.Field(base=Giveaway)
	giveaway_winners: GiveawayWinners = fields.ListField(base=GiveawayWinners)
	invoice: Invoice = fields.Field(base=Invoice)
	location: Location = fields.Field(base=Location)
	poll: Poll = fields.Field(base=Poll)
	venue: Venue = fields.Field(base=Venue)
