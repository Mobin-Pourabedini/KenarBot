import sys
from typing import Optional
from .message_handler import ChatBotMessageHandler
from .types.inline_keyboard import InlineKeyboardMarkup
from flask import Flask, request, Response
import httpx
import logging

from .types import ChatBotMessage


logging.basicConfig()
logger = logging.getLogger("kenarBot")

class KenarBot:
    def __init__(self, divar_identification_key: str, webhook_url: str, x_api_key: str):
        self.divar_identification_key = divar_identification_key
        self.webhook_url = webhook_url
        self.x_api_key = x_api_key
        self.message_handlers = []
        self.client = httpx.Client(headers={
            'Content-Type': 'application/json',
            'X-Api-Key': self.x_api_key
        })

    def send_message(self, conversation_id: str, message: str, keyboard_markup: Optional[InlineKeyboardMarkup] = None):
        url = 'https://api.divar.ir/experimental/open-platform/chatbot-conversations/{conversation_id}/messages'
        url = url.format(conversation_id=conversation_id)

        payload = {
            "type": "TEXT",
            "text_message": message,
        }
        if keyboard_markup is not None:
            payload["buttons"] = keyboard_markup.to_dict()

        response = self.client.post(url, json=payload)

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

    def run(self, host='0.0.0.0', port=80, debug=False):
        if debug:
            logger.setLevel(logging.DEBUG)
        app = Flask(__name__)

        @app.route(self.webhook_url, methods=['POST'])
        def webhook():
            headers = request.headers
            logger.info(f"headers: {headers}")
            if headers.get('Authorization') != self.divar_identification_key:
                return Response('{"message": "unauthorized request"}', status=403)
            data = request.get_json()
            logger.info(f"data: {data}")
            if data.get('type') != 'NEW_CHATBOT_MESSAGE':
                return Response(
                    '{"message": "message sent to chatbot webhook is not of form \"NEW_CHATBOT_MESSAGE\""}',
                    status=200)
            chatbot_message = data.get('new_chatbot_message')
            if not chatbot_message:
                return Response(
                    '{"message": "message sent to chatbot does not have key \"new_chatbot_message\""}',
                    status=200)
            if chatbot_message.get('type') != 'TEXT':
                return Response('{"message": "message type not supported for processing"}', status=200)
            text = chatbot_message.get('text')
            conversation_id = chatbot_message.get('conversation').get('id')
            self._process_new_chatbot_message(ChatBotMessage(text, conversation_id))
            return Response('{"message": "message processed"}', status=200)

        app.run(host=host, port=port, debug=debug)