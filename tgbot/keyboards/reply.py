from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
"""Клавиатура для выбора сценариев"""
class Main_menu():
    main_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    main_choice.row(KeyboardButton(text="Подбор запчастей"))
    main_choice.row(KeyboardButton(text="Автосервис"))
    main_choice.row(KeyboardButton(text="Кузовной ремонт"))
    main_choice.row(KeyboardButton(text="Автостраховка"))

"""Клавиатура для выбора услуг сервиса"""
class Serves_menu():
    serves_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    serves_choice.row(KeyboardButton(text="Шиномонтаж"))
    serves_choice.row(KeyboardButton(text="Мойка"))
    serves_choice.row(KeyboardButton(text="Диагностика подвестки"))
    serves_choice.row(KeyboardButton(text="Компьютерная диагностика"))
    serves_choice.row(KeyboardButton(text="Развал схождение"))
    serves_choice.row(KeyboardButton(text="Записаться на ремонт"))  

"""Клавиатура для того, чтобы поделиться номером"""
class User_phone:
    phone = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
    phone.row(KeyboardButton(text="Поделиться номером", request_contact=True))

"""Клавиатура для выбора СТО компании"""
class STO:
    sto = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
    sto.row(KeyboardButton(text="Фольсваген, Шкода"))
    sto.row(KeyboardButton(text="Рено"))
    sto.row(KeyboardButton(text="Хонда, Уаз"))
    sto.row(KeyboardButton(text="Джили"))

"""Клавиатура для выбора ответов Да или Нет"""
class Choice_user:
    user_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True) 
    user_choice.row(KeyboardButton(text="Да"))
    user_choice.row(KeyboardButton(text="Нет"))

class Choice_user_yes:
    user_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True) 
    user_choice.row(KeyboardButton(text="Да"))

"""Клавиатура для выбора услуг КМЦ"""
class Bodywork_menu():
    bodywork_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    bodywork_choice.row(KeyboardButton(text="Полировка"))
    bodywork_choice.row(KeyboardButton(text="Покраска"))
    bodywork_choice.row(KeyboardButton(text="Другие работы"))

"""Клавиатура для выбора услуг Страховой"""
class Insurance_menu():
    incurance_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    incurance_choice.row(KeyboardButton(text="КАСКО"))
    incurance_choice.row(KeyboardButton(text="ОСАГО"))
    incurance_choice.row(KeyboardButton(text="И КАСКО, и ОСАГО"))

"""Клавиатура для выбора места регестрации"""
class Insurance_menu_place():
    incurance_place = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    incurance_place.row(KeyboardButton(text="Волгоград"))
    incurance_place.row(KeyboardButton(text="Волгоградская область"))

"""Клавиатура для выбора места регестрации"""
class Insurance_choice():
    incurance_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    incurance_choice.row(KeyboardButton(text="Да"))
    incurance_choice.row(KeyboardButton(text="Не уверен"))
    incurance_choice.row(KeyboardButton(text="Нет"))

 

 

