from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.misc.states import Main_states
from tgbot.keyboards.reply import Bodywork_menu, User_phone 
import smtplib as smtp

from tgbot.handlers.password import E_MAIL_LOGIN, E_MAIL_OUT,E_MAIL_PASSWORD

ser_phone = []
time = []
user_name = []
adress = ["г. Волгоград, ул. Землячки 82г"]
working = []

def send_email(text):
   
    email = E_MAIL_LOGIN
    password = E_MAIL_PASSWORD
    dest_email = E_MAIL_OUT
    subject = 'Test'
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


async def bodywork(message: types.Message, state: None):
    text = [
        "выберете услугу",

    ]
    await message.answer('\n'.join(text), reply_markup=Bodywork_menu.bodywork_choice )
    await Main_states.Q3.set()

async def user_phone_bodywork(message: types.Message, state: FSMContext):
    text = [
        "Укажите свой номер телефона в формате +7999999999",
        "Или поделитесь"
    ]
    working.append(message.text)
    await message.answer('\n'.join(text), reply_markup=User_phone.phone )
    await Main_states.Q3_1.set()

async def user_user_contact(message: types.Message, state: FSMContext):
    ser_phone.append(message.contact.phone_number)
    text = [
        "Укажите время на которое хотели приехать",
    ]
    await message.answer('\n'.join(text))
    await Main_states.Q3_2.set()
async def user_phone_bodywork_text(message: types.Message, state: FSMContext):
    try:
        ser_phon1 = ""
        ser_phon1 = message.text.find('+7')   
    except:
        ser_phon1=-1
    if ser_phon1 != -1:
        await message.answer(text = "Укажите время на которое хотели приехать")
        await Main_states.Q3_2.set()
        ser_phone.append(message.contact.phone_number)    
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")

async def time_registr(message: types.Message, state: FSMContext):
    time.append(message.text)
    text = [
        "Укажите своё имя",
    ]   
    await message.answer('\n'.join(text))
    await Main_states.Q3_3.set() 

async def user_date_serves(message: types.Message, state: FSMContext,):
    user_name.append(message.text)
    text = [
        "Сообщение:\n",
        f"Работы : {working}\n"
        f"Ваше имя:{user_name}\n",
        f"Ваш телефон: {ser_phone}\n"
        f"Запись на:{time}\n",
        f"Адресс: {adress}\n",
        "Мы отправили ваши данные оператору\n",
        "Для возварашения в начало нажмите /start"
        ]
    await message.answer('\n'.join(text))
    text = [
        "Сообщение: Кузовной ремонт\n",
        f"Работы : {working[0]}\n",
        f"Ваше имя: {user_name[0]}\n",
        f"Ваш телефон: {ser_phone[0]}\n"
        f"Запись на: {time[0]}\n",
        f"Адресс: {adress[0]}\n"
    ]
    text=str(text)
    send_email(text)
    working.clear()
    user_name.clear()
    ser_phone.clear()
    time.clear()
    adress.clear()

def register_bodywork(dp: Dispatcher):
    dp.register_message_handler(bodywork, state='*', text=["Кузовной ремонт"])
    dp.register_message_handler(user_phone_bodywork, state=Main_states.Q3, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_user_contact, state=Main_states.Q3_1, content_types=["contact"])
    dp.register_message_handler(user_phone_bodywork_text, state=Main_states.Q3_1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(time_registr, state=Main_states.Q3_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_date_serves, state=Main_states.Q3_3, content_types=types.ContentTypes.ANY)