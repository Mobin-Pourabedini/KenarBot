import json
from typing import List, Optional

from .icons import Icon
from .actions import Action


class InlineKeyboardMarkup:
    max_rows = 3
    max_buttons_per_row = 3

    def __init__(self):
        self.keyboard: List[List[InlineKeyboardButton]] = []

    def row(self, *args: 'InlineKeyboardButton') -> 'InlineKeyboardMarkup':
        if len(args) == 0:
            return self

        if len(args) > self.max_buttons_per_row:
            raise ValueError(f"Maximum number of buttons per row is {self.max_buttons_per_row}")

        if len(self.keyboard) == self.max_rows:
            raise ValueError(f"Maximum number of rows is {self.max_rows}")

        for button in args:
            if not isinstance(button, InlineKeyboardButton):
                raise ValueError("All arguments must be of type InlineKeyboardButton")

        button_row = [button for button in args]
        self.keyboard.append(button_row)
        return self

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "rows": [{"buttons": [button.to_dict() for button in row]} for row in self.keyboard]
        }


class InlineKeyboardButton:
    def __init__(self, text: str, action: Action, icon: Optional[Icon] = None):
        if not text:
            raise ValueError("Button text must not be empty")
        if not isinstance(action, Action):
            raise ValueError("Button action must be of type Action")

        self.text: str = text
        self.action: Action = action
        self.icon: Icon = icon

    def to_dict(self):
        return {
            "action": self.action.to_dict(),
            "caption": self.text,
            "icon": str(self.icon)
        }
