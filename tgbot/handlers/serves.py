from distutils.command.config import config
from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext
from environs import Env
from tgbot.config import Config, TgBot

from tgbot.misc.states import Main_states
from tgbot.keyboards.reply import Serves_menu,User_phone, STO, Choice_user_yes
import smtplib as smtp
from tgbot.handlers.password import E_MAIL_LOGIN, E_MAIL_OUT,E_MAIL_PASSWORD
from tgbot.bd_bot.sql import  insert_data, view_data_id, view_data_phone, view_data_name


ser_phone = []
time = []
user_name = []
adress = []
working = []

def send_email(text):
   
    email = E_MAIL_LOGIN
    password = E_MAIL_PASSWORD
    dest_email = E_MAIL_OUT
    subject = 'Автосервис Телеграм'
    email_text = text

    mess = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                        dest_email, 
                                                        subject, 
                                                        email_text).encode('windows-1251').strip()
    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, dest_email, mess)
    server.quit()

  
   
    
async def serves(message: types.Message, state: None):
    text = [
        "выберете услугу",

    ]
    await message.answer('\n'.join(text), reply_markup=Serves_menu.serves_choice )
    await Main_states.Q2.set()

async def user_phone_serves(message: types.Message, state: FSMContext):
    id = view_data_id(message.from_user.id)
    if id == message.from_user.id:
        user_name.append(view_data_name(message.from_user.id))
        ser_phone.append(view_data_phone(message.from_user.id))
        await message.answer(text = "Укажите, в какое время хотели бы приехать:")
        working.append(message.text)
        await Main_states.Q2_3.set()
    else:
        text = [
            "Укажите свой номер телефона в формате +7999999999",
            "Или поделитесь"
        ]
        working.append(message.text)
        await message.answer('\n'.join(text), reply_markup=User_phone.phone )
        await Main_states.Q2_1.set()

async def user_user_contact(message: types.Message, state: FSMContext):
    ser_phone.append(message.contact.phone_number)
    text = [
        f"Ваше имя - {message.from_user.first_name}\n Если это так нажмите кнопку да\n Иначе напишите его"
    ]
    await message.answer('\n'.join(text),reply_markup=Choice_user_yes.user_choice)
    await Main_states.Q2_2.set()

async def user_phone_serves_text(message: types.Message, state: FSMContext):
    try:
        ser_phon1 = ""
        ser_phon1 = message.text.find('+7')        
    except:
        ser_phon1=-1
    if ser_phon1 != -1:
        await message.answer(text = f"Ваше имя - {message.from_user.first_name}\n Если это так нажмите кнопку да\n Иначе напишите его",reply_markup= Choice_user_yes.user_choice)
        await Main_states.Q2_2.set()
        ser_phone.append(message.text) 
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")


async def user_registor(message: types.Message, state: FSMContext):
    user_name.append(message.from_user.first_name)
    text = [
        "Укажите, в какое время хотели бы приехать:",
    ]   
    await message.answer('\n'.join(text))
    await Main_states.Q2_3.set() 

async def time_registr(message: types.Message, state: FSMContext):
    user_name.append(message.text)
    text = [
        "Укажите, в какое время хотели бы приехать:",
    ]   
    await message.answer('\n'.join(text))
    await Main_states.Q2_3.set() 

async def serves_sto(message: types.Message, state: FSMContext):
    time.append(message.text)
    text = [
        "Выберете интересующую СТО",
    ]
    await message.answer('\n'.join(text),reply_markup=STO.sto)
    await Main_states.Q2_4.set()


async def user_date_serves(message: types.Message, state: FSMContext,):

    if message.text == "Фольсваген, Шкода":
        adress.append("г. Волгоград, ул. Землячки 82г")
    elif message.text == "Рено":
        adress.append("г. Волгоград, ул. Землячки 67")
    elif message.text == "Хонда, Уаз":
        adress.append("г. Волгоград, ул. Карла Либкнехта 19а")
    elif message.text == "Джили":
        adress.append("г. Волгоград, ул. Землячки 69")

    text = [
        "Сообщение:\n",
        f"Работы : {working[0]}\n",
        f"Ваше имя: {user_name[0]}\n",
        f"Ваш телефон: {ser_phone[0]}\n"
        f"Запись на: {time[0]}\n",
        f"Адресс: {adress[0]}\n",
        "Мы отправили ваши данные оператору\n",
        "Для возварашения в начало нажмите /start"
        ]        
    await message.answer('\n'.join(text))
    id = view_data_id(message.from_user.id)
    if id != message.from_user.id:
        insert_data(message.from_user.id,user_name[0],ser_phone[0])
    text = f"Сообщение:Запись на сервис\n Работы : {working[0]}\n Ваше имя: {user_name[0]}\n Ваш телефон: {ser_phone[0]}\n Запись на: {time[0]}\n Адресс: {adress[0]}\n"
    
    text=str(text)
    send_email(text)
    
    working.clear()
    user_name.clear()
    ser_phone.clear()
    time.clear()
    adress.clear()


def register_serves(dp: Dispatcher):
    dp.register_message_handler(serves, text=["Автосервис"])
    dp.register_message_handler(user_phone_serves, state=Main_states.Q2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_user_contact, state=Main_states.Q2_1, content_types=["contact"])
    dp.register_message_handler(user_phone_serves_text, state=Main_states.Q2_1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_registor, state=Main_states.Q2_2, content_types=["Да"])
    dp.register_message_handler(time_registr, state=Main_states.Q2_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(serves_sto, state=Main_states.Q2_3, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_date_serves, state=Main_states.Q2_4, content_types=types.ContentTypes.ANY)