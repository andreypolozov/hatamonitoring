import typing as tp
import telebot

from .config import CONFIG
from .markups import Murkups
from .utils import get_token
from .view import API

bot = telebot.TeleBot(token=get_token())


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text=CONFIG["START_MESSAGE"],
        reply_markup=Murkups.MAIN_MENU.value
    )


# Default handler
@bot.message_handler()
def main_handler(message: telebot.types.Message):
    chat_id = message.chat.id
    if message.text not in API:
        print(f"Command {message.text} not in API")
        return
    result = API[message.text]()
    if result:
        bot.send_message(
            chat_id=chat_id,
            text=result.text,
            reply_markup=result.next_markup
        )
