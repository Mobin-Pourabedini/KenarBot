import os

from src.kenarBot.app import KenarBot
from src.kenarBot.types import ChatBotMessage

DIVAR_API_KEY = os.getenv("DIVAR_API_KEY")
DIVAR_IDENTIFICATION_KEY = os.getenv("DIVAR_IDENTIFICATION_KEY")

bot = KenarBot(DIVAR_IDENTIFICATION_KEY, "/webhook", DIVAR_API_KEY)


@bot.message_handler(regexp="hello .*")
def handle_hello(chatbot_message: ChatBotMessage):
    bot.send_message(chatbot_message.conversation_id, f"you said {chatbot_message.message}")


if __name__ == "__main__":
    bot.run()
