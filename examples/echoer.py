import os

from src.kenarBot.app import KenarBot
from src.kenarBot.types import ChatBotMessage
from src.kenarBot.types.actions import OpenDirectLink, OpenServerLink
from src.kenarBot.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from src.kenarBot.types.icons import Icon

DIVAR_API_KEY = os.getenv("DIVAR_API_KEY")
DIVAR_IDENTIFICATION_KEY = os.getenv("DIVAR_IDENTIFICATION_KEY")

bot = KenarBot(DIVAR_IDENTIFICATION_KEY, "/webhook", DIVAR_API_KEY)


@bot.message_handler(regexp="hello .*")
def handle_hello(chatbot_message: ChatBotMessage):
    action = OpenDirectLink("https://your.website.com")
    action2 = OpenServerLink({"key_1": "value_1"})
    b1 = InlineKeyboardButton("button 1", action, Icon.HOME)
    b2 = InlineKeyboardButton("button 2", action2, Icon.CALL)
    keyboard = InlineKeyboardMarkup().row(b1, b2)
    bot.send_message(
        chatbot_message.conversation_id,
        f"you said {chatbot_message.message}",
        keyboard_markup=keyboard)


if __name__ == "__main__":
    bot.run(port=5001, debug=True)
