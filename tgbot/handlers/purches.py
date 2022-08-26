from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import Choice_user_yes, User_phone, last_menu
from tgbot.misc.states import Main_states
import smtplib as smtp
from tgbot.handlers.password import E_MAIL_LOGIN, E_MAIL_OUT,E_MAIL_PASSWORD
from tgbot.bd_bot.sql import  insert_data, view_data_id, view_data_phone, view_data_name

user_name = []
pur_phon = []
articul = []
VIN = []


def send_email(text):
   
    email = E_MAIL_LOGIN
    password = E_MAIL_PASSWORD
    dest_email = E_MAIL_OUT
    subject = 'ОЗЧ Телеграм'
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


async def purches(message: types.Message, state: None):
    id = view_data_id(message.from_user.id)
    if id == message.from_user.id:
        user_name.append(view_data_name(message.from_user.id))
        pur_phon.append(view_data_phone(message.from_user.id))
        await message.answer(text = "Напишите название запчасти или артикул запчасти",reply_markup=types.ReplyKeyboardRemove())
        await Main_states.Q1_2.set()
    else:   
        text = [
            "Укажите свой номер телефона в формате +7999999999",
            "Или поделитесь"
        ]
        await message.answer('\n'.join(text), reply_markup= User_phone.phone)
        await Main_states.Q1.set()


async def user_contact(message: Message, state: FSMContext):
    await message.answer(text =  f"Ваше имя - {message.from_user.first_name}\n Если это так нажмите кнопку да\n Иначе напишите его",reply_markup= Choice_user_yes.user_choice)
    pur_phon.append("+" + message.contact.phone_number)
    await Main_states.Q1_1.set()

async def user_contact_text(message: Message, state: FSMContext):
    try:
        pur_phone = message.text.find('+7')
    except:
        pur_phone=-1
    if pur_phone != -1:
        await message.answer(text = f"Ваше имя - {message.from_user.first_name}\n Если это так нажмитt кнопку да\n Иначе напишите его",reply_markup= Choice_user_yes.user_choice)
        await Main_states.Q1_1.set()
        pur_phon.append(message.text)
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")

async def name_user_yes(message: Message, state: FSMContext):
    await message.answer(text = "Напишите название запчасти или артикул запчасти",reply_markup=types.ReplyKeyboardRemove())
    user_name.append(message.from_user.first_name)
    await Main_states.Q1_2.set()

async def name_user(message: Message, state: FSMContext):
    await message.answer(text = "Напишите название запчасти или артикул запчасти",reply_markup=types.ReplyKeyboardRemove())
    user_name.append(message.from_user.first_name)
    await Main_states.Q1_2.set()

async def name_purches(message: Message, state: FSMContext):
    await message.answer(text = "Для подбора автозапчасти необходим VIN номер автомобиля. Введите пожайлуста.",reply_markup=types.ReplyKeyboardRemove())
    articul.append(message.text)
    await Main_states.Q1_3.set()

async def purches_end(message: Message, state: FSMContext):
    await message.answer(text = "Наш специалист проверит наличие или возможность заказа запчасти и связжеться с Вами.\n Для возврата нажмите /start", reply_markup= last_menu.choice)
    VIN.append(message.text)
    await state.finish()
    text = f"Сообщение: Телеграм Бот;\r\n Работы : ОЗПЧ;\r\n  Имя клиента: {user_name[0]};\r\n  телефон: {pur_phon[0]};\r\n Название запчасти или артикул запчасти: {articul[0]};\r\n VIN номер автомобиля: {VIN[0]};\r\n"
    id = view_data_id(message.from_user.id)
    if id != message.from_user.id:
        insert_data(message.from_user.id,user_name[0],pur_phon[0])
    text=str(text)
    send_email(text)
    user_name.clear()
    pur_phon.clear()
    articul.clear()
    VIN.clear()


def register_purches(dp: Dispatcher):
    dp.register_message_handler(purches, text=["Подбор запчастей"])
    dp.register_message_handler(user_contact, state=Main_states.Q1, content_types=["contact"])
    dp.register_message_handler(user_contact_text, state=Main_states.Q1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(name_user_yes, state=Main_states.Q1_1, content_types=["Да"])
    dp.register_message_handler(name_user, state=Main_states.Q1_1, content_types=types.ContentTypes.ANY) 
    dp.register_message_handler(name_purches, state=Main_states.Q1_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(purches_end, state=Main_states.Q1_3, content_types=types.ContentTypes.ANY)