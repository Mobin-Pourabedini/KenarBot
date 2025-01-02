import pytest

from src.kenarBot.types.inline_keyboard import InlineKeyboardButton
from src.kenarBot.types.actions import OpenDirectLink
from src.kenarBot.types.icons import Icon

class TestInlineKeyboardButton:
    def setup_method(self):
        print("setup method")
        self.correct_action = OpenDirectLink("https://google.com")
        self.correct_icon = Icon.HOME
        self.correct_text = "text"
        pass

    def test_init(self):
        button = InlineKeyboardButton(self.correct_text, self.correct_action)
        assert button.text == self.correct_text
        assert button.action == self.correct_action
        assert button.icon is None

    def test_init_with_icon(self):
        button = InlineKeyboardButton(self.correct_text, self.correct_action, self.correct_icon)
        assert button.text == self.correct_text
        assert button.action == self.correct_action
        assert button.icon == self.correct_icon

    def test_init_empty_text(self):
        with pytest.raises(ValueError) as e:
            InlineKeyboardButton("", self.correct_action)
            assert str(e.value) == "Button text must not be empty"

    def test_init_empty_action(self):
        with pytest.raises(ValueError) as e:
            InlineKeyboardButton(self.correct_text, "")
            assert str(e.value) == "Button action must be of type Action"

    def test_to_dict(self):
        button = InlineKeyboardButton(self.correct_text, self.correct_action, self.correct_icon)
        assert button.to_dict() == {
            "action": self.correct_action.to_dict(),
            "caption": self.correct_text,
            "icon": str(self.correct_icon)
        }
