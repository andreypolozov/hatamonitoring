import typing as tp
from dataclasses import dataclass

import telebot

from .dao import DataBaseDao
from .markups import Commands, Murkups

dao = DataBaseDao()

@dataclass
class ApiResponse:
    text: str
    next_markup: telebot.types.ReplyKeyboardMarkup = Murkups.MAIN_MENU.value

def wrap_api_response(object):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return ApiResponse(result, object)
        return wrapper
    return decorator

@wrap_api_response(Murkups.MAIN_MENU.value)
def switch_duty():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка свитч дюте"

@wrap_api_response(Murkups.MAIN_MENU.value)
def change_able():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка абля"

@wrap_api_response(Murkups.MAIN_MENU.value)
def duty_list():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка duty_list"

@wrap_api_response(Murkups.MAIN_MENU.value)
def get_users():
    return f"Челики: " + "\n".join([f"id: {_id}, name: {_name}" for _id, _name in dao.get_users()])

@wrap_api_response(Murkups.MAIN_MENU.value)
def current_duty():
    return str(dao.curren_duty())


@wrap_api_response(Murkups.MAIN_MENU.value)
def cancel():
    return "Покакал"

API = {
    Commands.DUTY_TABLE.value: duty_list,
    Commands.SWITCH_DUTY.value: switch_duty,
    Commands.USERS.value: get_users,
    Commands.CANCEL.value: cancel,
}