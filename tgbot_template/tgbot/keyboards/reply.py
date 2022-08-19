from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
class Main_menu():
    main_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    main_choice.row(KeyboardButton(text="Подбор запчастей"))
    main_choice.row(KeyboardButton(text="Автосервис"))
    main_choice.row(KeyboardButton(text="Кузовной ремонт"))
    main_choice.row(KeyboardButton(text="Автостраховка"))
    main_choice.row(KeyboardButton(text="Позвать оператора"))  

class Serves_menu():
    serves_choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)

    serves_choice.row(KeyboardButton(text="Шиномонтаж"))
    serves_choice.row(KeyboardButton(text="Мойка"))
    serves_choice.row(KeyboardButton(text="Диагностика подвестки"))
    serves_choice.row(KeyboardButton(text="Компьютерная диагностика"))
    serves_choice.row(KeyboardButton(text="Развал схождение"))
    serves_choice.row(KeyboardButton(text="Записаться на ремонт")) 
    serves_choice.row(KeyboardButton(text="Позвать оператора"))  

class User_phone:
    phone = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
    phone.row(KeyboardButton(text="Поделиться номером", request_contact=True))

class STO:
    sto = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
    sto.row(KeyboardButton(text="Фольсваген"))
    sto.row(KeyboardButton(text="Рено"))
    sto.row(KeyboardButton(text="Шкода, Хонда, Уаз"))
    sto.row(KeyboardButton(text="Джили"))

