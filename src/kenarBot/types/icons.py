from enum import Enum


class Icon(Enum):
    # Navigation and Basic Actions
    KEYBOARD_ARROW_RIGHT = "KEYBOARD_ARROW_RIGHT"
    KEYBOARD_ARROW_LEFT = "KEYBOARD_ARROW_LEFT"
    ARROW_FORWARD = "ARROW_FORWARD"
    REFRESH = "REFRESH"
    REMOVE = "REMOVE"
    SEND = "SEND"
    DELETE = "DELETE"
    ADD = "ADD"
    CLOSE = "CLOSE"
    EDIT = "EDIT"
    CANCEL = "CANCEL"

    # Status and Information
    WARNING = "WARNING"
    INFO = "INFO"
    INFO_OUTLINE = "INFO_OUTLINE"
    HELP = "HELP"
    HELP_OUTLINE = "HELP_OUTLINE"
    CHECK_CIRCLE = "CHECK_CIRCLE"
    ERROR = "ERROR"
    VERIFIED = "VERIFIED"

    # Media and Files
    PHOTO_LIBRARY = "PHOTO_LIBRARY"
    IMAGE_OUTLINE = "IMAGE_OUTLINE"
    VIDEOCAM = "VIDEOCAM"
    FILE = "FILE"
    DOWNLOAD = "DOWNLOAD"

    # Communication
    CHAT_BUBBLE = "CHAT_BUBBLE"
    EMAIL_OUTLINE = "EMAIL_OUTLINE"
    CALL = "CALL"
    CONTACT_PHONE = "CONTACT_PHONE"

    # User Interface
    SETTINGS = "SETTINGS"
    SEARCH = "SEARCH"
    FILTER = "FILTER"
    MORE_VERT = "MORE_VERT"
    VISIBILITY = "VISIBILITY"
    LOCK = "LOCK"

    # User and Account
    PERSON = "PERSON"
    PERSON_ADD = "PERSON_ADD"
    EXIT_TO_APP = "EXIT_TO_APP"
    LOGOUT = "LOGOUT"

    # Social and Sharing
    SHARE = "SHARE"
    BOOKMARK = "BOOKMARK"
    BOOKMARK_BORDER = "BOOKMARK_BORDER"
    STAR = "STAR"
    STAR_BORDER = "STAR_BORDER"

    # Business and Commerce
    PAYMENT = "PAYMENT"
    MONEY = "MONEY"
    SHOPPING = "SHOPPING"
    CART = "CART"
    STORE = "STORE"

    # Time and Schedule
    ACCESS_TIME = "ACCESS_TIME"
    EVENT_NOTE = "EVENT_NOTE"
    CALENDAR = "CALENDAR"
    TIMER = "TIMER"

    # Location
    PLACE = "PLACE"
    MAP_MARKER = "MAP_MARKER"
    HOME = "HOME"

    # Analytics
    SHOW_CHART = "SHOW_CHART"
    TRENDING_UP = "TRENDING_UP"
    ANALYTICS = "ANALYTICS"

    # Misc
    SUPPORT = "SUPPORT"
    NOTE = "NOTE"
    GIFT = "GIFT"
    LAUNCH = "LAUNCH"

    @classmethod
    def list(cls):
        """Returns a list of all available icon values"""
        return [member.value for member in cls]

    @classmethod
    def has_value(cls, value):
        """Check if a value exists in the enum"""
        return value in cls.list()

    @classmethod
    def from_string(cls, value: str):
        """Convert a string to an enum member"""
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid IconType")

    def __str__(self):
        return self.value
