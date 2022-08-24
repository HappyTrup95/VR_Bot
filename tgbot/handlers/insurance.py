from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import STO, Insurance_menu_place, User_phone, Insurance_menu
from tgbot.misc.states import Main_states
from tgbot.handlers.password import E_MAIL_LOGIN, E_MAIL_OUT,E_MAIL_PASSWORD
from tgbot.bd_bot.sql import  insert_data, view_data_id, view_data_phone, view_data_name

import smtplib as smtp

working = []
ser_phone = []
user_name = []
place = []
adress = []
avto = []

def send_email(text):
   
    email = E_MAIL_LOGIN
    password = E_MAIL_PASSWORD
    dest_email = E_MAIL_OUT
    subject = 'Страхование Телеграм'
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

async def insurance(message: types.Message, state: None):
    text = ["Выберете услугу"]
    await message.answer('\n'.join(text), reply_markup=Insurance_menu.incurance_choice )
    await Main_states.Q4.set()

async def insurance_bd(message: types.Message, state: None):
    id = view_data_id(message.from_user.id)
    if id == message.from_user.id:
        user_name.append(view_data_name(message.from_user.id))
        ser_phone.append(view_data_phone(message.from_user.id))
        await message.answer(text = "Прописка у вас г. Волгоград или Волгоградская область",reply_markup=Insurance_menu_place.incurance_place)
        working.append(message.text)
        await Main_states.Q4_2.set()
    else:
        text = ["Выберете услугу"]
        working.append(message.text)
        await message.answer('\n'.join(text), reply_markup=Insurance_menu.incurance_choice )
        await Main_states.Q4_1.set()

async def user_phone_insurance(message: types.Message, state: None):
    text = [
        "Укажите свой номер телефона в формате +7999999999",
        "Или поделитесь"
        ]
    working.append(message.text)
    await message.answer('\n'.join(text), reply_markup=User_phone.phone )
    await Main_states.Q4_2.set()

async def user_insurance_contact(message: types.Message, state: FSMContext):
    ser_phone.append(message.contact.phone_number)
    text = [
        "Прописка у вас г. Волгоград или Волгоградская область",
    ]
    await message.answer('\n'.join(text), reply_markup=Insurance_menu_place.incurance_place)
    await Main_states.Q4_3.set()

async def user_phone_insurance_text(message: types.Message, state: FSMContext):
    try:
        ser_phon1 = ""
        ser_phon1 = message.text.find('+7')        
    except:
        ser_phon1=-1
    if ser_phon1 != -1:
        await message.answer(text = "Прописка у вас г. Волгоград или Волгоградская область",reply_markup=Insurance_menu_place.incurance_place)
        await Main_states.Q4_3.set()
        ser_phone.append(ser_phon1) 
    else:
        await message.answer(text = "Неверная команда, попробуйте снова", reply_markup=Insurance_menu_place.incurance_place)


async def place_answer_1(message: types.Message, state: FSMContext):
    place.append(message.text)
    await message.answer(text = "На какое СТО хотите приехать?", reply_markup= STO.sto)
    await Main_states.Q4_3.set()

async def name_insuranse(message: types.Message, state: FSMContext):
    adress.append(message.text)
    await message.answer(text = "Пропишите марку и модель автомобиля для того, чтобы мы не запутались в ваших автомобилях")
    await Main_states.Q4_4.set()

async def name_insuranse1(message: types.Message, state: FSMContext):
    avto.append(message.text)
    await message.answer(text = "Отлично! Всё готово\n Я передам всю информацию нашему сотруднику в отдел страхования. А он с вами свяжеться и все подробно расскажет.\n Для возврата нажмите /start")
    text = f"Сообщение: Страховка;\n Работы : {working[0]};\n Имя клиента: {user_name[0]};\n телефон: {ser_phone[0]};\n Регистрация: {place[0]};\n Адресс: {adress[0]};\n Марка авто: {avto[0]};\n"
    
    id = view_data_id(message.from_user.id)
    if id != message.from_user.id:
        insert_data(message.from_user.id,user_name[0],ser_phone[0])

    send_email(text)

    working.clear()
    user_name.clear()
    ser_phone.clear()
    place.clear()
    adress.clear()
    avto.clear()

def register_insurance(dp: Dispatcher):
    dp.register_message_handler(insurance, text=["Автостраховка"])
    dp.register_message_handler(insurance_bd, state=Main_states.Q4, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_insurance_contact, state=Main_states.Q4_1, content_types=["contact"])
    dp.register_message_handler(user_phone_insurance_text, state=Main_states.Q4_1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(place_answer_1, state=Main_states.Q4_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(name_insuranse, state=Main_states.Q4_3, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(name_insuranse1, state=Main_states.Q4_4, content_types=types.ContentTypes.ANY)