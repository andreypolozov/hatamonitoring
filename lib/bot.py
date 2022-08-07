import typing as tp
import telebot

from .config import CONFIG
from .markups import MARKUPS
from .utils import get_token

bot = telebot.TeleBot(token=get_token())


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text=CONFIG["START_MESSAGE"],
        reply_markup=MARKUPS["MAIN_MENU"]
    )


# Default handler
@bot.message_handler()
def main_handler(message: telebot.types.Message):
    chat_id = message.chat.id
    # if message.text == :
    bot.send_message(
        chat_id=chat_id, text=f"Как зовут лоха?", reply_markup=MARKUPS["DUMMY"])
