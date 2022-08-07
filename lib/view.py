from dao import DataBaseDao

# TODO: 
# dao = DataBaseDao(Тут аргументы для авторизации)

def switch_duty():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка свитч дюте"

def change_able():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка абля"

def duty_list():
    "Дёргаем dao и форматируем ответ"
    return f"Ручка duty_list"


API = {
    "Список дежурств": duty_list,
    "Поменяться дежурством": switch_duty,
    
}