import enum
import telebot


class Commands(enum.Enum):
    USERS="Список пользователей"
    DUTY_TABLE="Список деружств"
    SWITCH_DUTY="Поменяться дежурством"
    MY_DUTY="Мои дежурства"
    MY_ABLES="Мои отсутствия"
    CANCEL="Отмена"


def get_keyboard_markup():
    return telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

def main_menu_markup() -> telebot.types.ReplyKeyboardMarkup:
    markup = get_keyboard_markup()
    markup.row(Commands.DUTY_TABLE.value)
    markup.row(Commands.USERS.value)
    markup.row(Commands.CANCEL.value)
    return markup


def pokakal() -> telebot.types.ReplyKeyboardMarkup:
    markup = get_keyboard_markup()
    markup.row(Commands.SWITCH_DUTY.value)
    markup.row(Commands.CANCEL.value)
    return markup


def dummy() -> telebot.types.ReplyKeyboardMarkup:
    markup = get_keyboard_markup()
    return markup


class Murkups(enum.Enum):
    MAIN_MENU = main_menu_markup()
    DUMMY = dummy()
    POKAKAL = pokakal()
