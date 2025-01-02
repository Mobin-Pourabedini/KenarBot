import pytest

from src.kenarBot.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from src.kenarBot.types.actions import OpenDirectLink


class TestInlineKeyboardMarkup:
    def setup_method(self):
        print("setup method")
        self.correct_button = InlineKeyboardButton("text", OpenDirectLink("https://google.com"))
        pass

    def test_init(self):
        markup = InlineKeyboardMarkup()
        assert markup.keyboard == []

    def test_row(self):
        markup = InlineKeyboardMarkup().row(self.correct_button)
        assert markup.keyboard == [[self.correct_button]]

    def test_row_max_buttons_per_row(self):
        with pytest.raises(ValueError) as e:
            InlineKeyboardMarkup().row(*[self.correct_button for _ in range(4)])
            assert str(e.value) == "Maximum number of buttons per row is 3"

    def test_row_max_rows(self):
        with pytest.raises(ValueError) as e:
            InlineKeyboardMarkup().row(*[self.correct_button for _ in range(4)]).row(self.correct_button)
            assert str(e.value) == "Maximum number of rows is 3"

    def test_row_empty(self):
        markup = InlineKeyboardMarkup().row()
        assert markup.keyboard == []

    def test_row_not_button(self):
        with pytest.raises(ValueError) as e:
            InlineKeyboardMarkup().row("not button")
            assert str(e.value) == "All arguments must be of type InlineKeyboardButton"

    def test_to_json(self):
        markup = InlineKeyboardMarkup().row(self.correct_button)
        assert markup.to_json() == ('{"rows": [{"buttons": [{"action": {"open_direct_link": "https://google.com"},'
                                    ' "caption": "text", "icon": "None"}]}]}')

    def test_to_dict_2_buttons_in_a_row(self):
        markup = InlineKeyboardMarkup().row(self.correct_button, self.correct_button)
        assert markup.to_dict() == {
            "rows": [
                {"buttons":
                    [
                        {"action": {"open_direct_link": "https://google.com"}, "caption": "text", "icon": "None"},
                        {"action": {"open_direct_link": "https://google.com"}, "caption": "text", "icon": "None"}
                    ]
                }
            ]
        }

    def test_to_dict_2_buttons_in_2_row(self):
        markup = InlineKeyboardMarkup().row(self.correct_button).row(self.correct_button)
        assert markup.to_dict() == {
            "rows": [
                {"buttons":
                    [
                        {"action": {"open_direct_link": "https://google.com"}, "caption": "text", "icon": "None"},
                    ]
                },
                {"buttons":
                    [
                        {"action": {"open_direct_link": "https://google.com"}, "caption": "text", "icon": "None"},
                    ]
                }
            ]
        }
