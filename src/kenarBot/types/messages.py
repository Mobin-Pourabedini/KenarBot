class ChatBotMessage:
    def __init__(self, message: str, conversation_id: str):
        self.message = message
        self.conversation_id = conversation_id

    def __str__(self):
        return f"Message: {self.message}, Conversation ID: {self.conversation_id}"
