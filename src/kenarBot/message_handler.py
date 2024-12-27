from typing import Optional, Callable
import re
from .types import ChatBotMessage


class ChatBotMessageHandler:
    def __init__(self, f: Callable, regexp: Optional[str] = None, ):
        self.function = f
        self.regexp = regexp

    def should_process(self, chatbot_message: ChatBotMessage):
        return re.match(self.regexp, chatbot_message.message) if self.regexp else True

    def process(self, message: ChatBotMessage):
        return self.function(message)
