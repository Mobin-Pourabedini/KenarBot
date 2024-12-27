from typing import Optional
from .message_handler import ChatBotMessageHandler
from flask import Flask, request, Response
import requests

from .types import ChatBotMessage


class KenarBot:
    def __init__(self, divar_identification_key: str, webhook_url: str, x_api_key: str):
        self.divar_identification_key = divar_identification_key
        self.webhook_url = webhook_url
        self.x_api_key = x_api_key
        self.message_handlers = []

    def send_message(self, conversation_id: str, message: str):
        url = 'https://api.divar.ir/experimental/open-platform/chatbot-conversations/{conversation_id}/messages'
        url = url.format(conversation_id=conversation_id)

        headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.x_api_key
        }

        payload = {
            "type": "TEXT",
            "text_message": message
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.status_code)
        print(response.json())

    def message_handler(self, regexp: Optional[str] = None):
        def decorator(f):
            self.message_handlers.append(ChatBotMessageHandler(f, regexp))
            return f

        return decorator

    def _process_new_chatbot_message(self, message: ChatBotMessage):
        for message_handler in self.message_handlers:
            if message_handler.should_process(message):
                message_handler.process(message)
                break

    def run(self):
        app = Flask(__name__)

        @app.route(self.webhook_url, methods=['POST'])
        def webhook():
            headers = request.headers
            if headers.get('Authorization') != self.divar_identification_key:
                return Response('{"message": "unauthorized request"}', status=403)
            data = request.get_json()
            if data.get('type') != 'NEW_CHATBOT_MESSAGE':
                return Response(
                    '{"message": "message sent to chatbot webhook is not of form \"NEW_CHATBOT_MESSAGE\""}',
                    status=400)
            chatbot_message = data.get('new_chatbot_message')
            if not chatbot_message:
                return Response(
                    '{"message": "message sent to chatbot does not have key \"new_chatbot_message\""}',
                    status=400)
            if chatbot_message.get('type') != 'TEXT':
                return Response('{"message": "message types other than text not supported"}', status=501)
            text = chatbot_message.get('message_text')
            conversation_id = chatbot_message.get('conversation').get('id')
            self._process_new_chatbot_message(ChatBotMessage(text, conversation_id))
            return Response('{"message": "message processed"}', status=200)

        app.run(debug=True)