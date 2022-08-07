import telebot


def main_menu_markup() -> telebot.types.ReplyKeyboardMarkup:
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Список")
    # markup.row("Отмена")
    return markup


def dummy() -> telebot.types.ReplyKeyboardMarkup:
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Кнопка")


MARKUPS = {
    "MAIN_MENU": main_menu_markup(),
    "DUMMY": dummy()
}
