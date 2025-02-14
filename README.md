# KenarBot

<div align="center">

[![PyPI version](https://badge.fury.io/py/kenarbot.svg)](https://badge.fury.io/py/kenarbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/kenarbot.svg)](https://pypi.org/project/kenarbot/)
[![codecov](https://codecov.io/github/Mobin-Pourabedini/KenarBot/graph/badge.svg)](https://codecov.io/github/Mobin-Pourabedini/KenarBot)
</div>

A Python SDK for creating and managing Kenar messaging bots. KenarpyBot provides a simple, intuitive interface inspired by teleBot's syntax, making it easy for developers familiar with Telegram bot development to create bots for the Kenar platform.

### What is Kenar Divar?
[Kenar Divar](https://github.com/divar-ir/kenar-docs) is Divar's official platform that provides APIs for developers to create
plugins and integrations with Divar. These APIs enable functionality like sending and receiving messages, editing posts, patching add-ons on posts and etc...
, you should also checkput [Kenar Divar Panel](https://divar.ir/kenar)

## Features

- 🚀 Simple, teleBot-inspired syntax
- 📨 Easy message handling and routing
- 🔄 Built-in support for Kenar's messaging endpoints
- ⚡ Flask-based webhook handling
- ⚙️ Straightforward bot configuration

## Examples
- [Cowsay echo bot](https://github.com/Mobin-Pourabedini/divar-echo-bot)

## Installation

```bash
pip install kenarbot
```

## Quick Start Example

Here's a simple example demonstrating how to create a bot that responds to messages containing "hello":

```python
import os

from kenarBot import KenarBot
from kenarBot.types import ChatBotMessage

# Initialize your API key from Kenar platform
DIVAR_API_KEY = os.getenv("DIVAR_API_KEY")
DIVAR_IDENTIFICATION_KEY = os.getenv("DIVAR_IDENTIFICATION_KEY")

# Create a bot instance
bot = KenarBot(DIVAR_IDENTIFICATION_KEY, "/webhook", DIVAR_API_KEY)

# Define a message handler that responds to messages containing "hello"
@bot.message_handler(regexp="hello")
def handle_hello(chatbot_message: ChatBotMessage):
    # Send a response back to the same conversation
    bot.send_message(chatbot_message.conversation_id, f"Hi, my name is AmazingKenarBot")

if __name__ == "__main__":
    # Start the bot
    bot.run()
```

This example shows:
- How to initialize the bot with your API key
- How to create a message handler using decorators
- How to respond to specific messages using regular expressions
- How to send messages back to conversations

### Key Components:

1. **Bot Initialization**:
   - Create a `KenarBot` instance with your app name, webhook path, and API key
   - The webhook path is where your bot will receive updates

2. **Message Handler**:
   - Use the `@bot.message_handler` decorator to define message handlers
   - The `regexp` parameter allows you to filter messages based on regular expressions
   - Other handler options are available (commands, content types, etc.)

3. **Sending Messages**:
   - Use `bot.send_message()` to send responses
   - Requires the conversation ID and the message text

4. **Running the Bot**:
   - Call `bot.run()` to start the bot
   - This will start a Flask server to handle incoming webhook requests

### Important Notes:
- Keep your API key secure and never commit it to version control
- Consider using environment variables for sensitive data
- The bot runs on Flask, so it needs to be hosted on a server accessible to Kenar

## Documentation

### Available Methods

- `bot.send_message(conversation_id, text)`: Send a message to a conversation
- `bot.message_handler(regexp="")`: Decorator for handling messages matching a regex pattern
- `bot.run()`: Start the bot's webhook server

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Create an [Issue](https://github.com/Mobin-Pourabedini/KenarBot/issues)
- Send an email to realmobinpourabedini@gmail.com

## Acknowledgments

- Inspired by the [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) project
- Thanks to the open-platform team

## Author

Mobin Pourabedini ([@Mobin-Pourabedini](https://github.com/Mobin-Pourabedini))

---

Made with ❤️ for the Kenar community
