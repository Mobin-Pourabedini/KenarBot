import json
from typing import List, Optional

from src.kenarBot.types.icons import Icon
from src.kenarBot.types.actions import Action


class InlineKeyboardMarkup:
    def __init__(self, row_width=3):
        self.keyboard: List[List[InlineKeyboardButton]] = []
        self.row_width = row_width

    def row(self, *args) -> 'InlineKeyboardMarkup':
        button_row = [button for button in args]
        self.keyboard.append(button_row)
        return self

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "rows" : [{"buttons": [button.to_dict() for button in row]} for row in self.keyboard]
        }


class InlineKeyboardButton:
    def __init__(self, text: str, action: Action, icon: Optional[Icon] = None):
        self.text: str = text
        self.action: Action = action
        self.icon: Icon = icon

    def to_dict(self):
        return {
            "action": self.action.to_dict(),
            "caption": self.text,
            "icon": str(self.icon)
        }
