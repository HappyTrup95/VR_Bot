from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext


from tgbot.misc.states import Main_states
from tgbot.keyboards.reply import Serves_menu,User_phone, STO 

ser_phone = ""
time = ""

async def serves(message: types.Message, state: None):
    text = [
        "выберете услугу",

    ]
    await message.answer('\n'.join(text), reply_markup=Serves_menu.serves_choice )
    await Main_states.Q2.set()

async def user_phone_serves(message: types.Message, state: FSMContext):
    text = [
        "Укажите свой номер телефона в формате +7999999999",
        "Или поделитесь"
    ]

    await message.answer('\n'.join(text), reply_markup=User_phone.phone )
    await Main_states.Q2_1.set()

async def user_phone_serves_text(message: types.Message, state: FSMContext):
    try:
        ser_phon = message.text.find('+7')
    except:
        ser_phon=-1
    if ser_phon != -1:
        await message.answer(text = "Напишите название запчасти или артикул запчасти")
        await Main_states.Q2_2.set()
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")


async def user_user_contact(message: types.Message, state: FSMContext, ser_phone: str):
    text = [
        "Укажите, как вас зовут",
    ]
    await message.answer('\n'.join(text))
    ser_phone=message.contact.phone_number
    await Main_states.Q2_2.set()

async def serves_sto(message: types.Message, state: FSMContext, time: str):
    text = [
        "Выберете своё СТО",
    ]
    await message.answer('\n'.join(text),reply_markup=STO.sto)
    await Main_states.Q2_3.set()
    time = message.text

async def user_date_serves(message: types.Message, state: FSMContext):
    text = [
        "Сообщение:",
        f"Ваше имя:{message.from_user.first_name}",
        f"Ваш телефон: {ser_phone}"
        f"Запись на:{time} ",
        f"Адресс: "
        "Всё верно?"
        ]
    await message.answer('\n'.join(text))



def register_serves(dp: Dispatcher):
    dp.register_message_handler(serves, text=["Автосервис"])
    dp.register_message_handler(user_phone_serves, state=Main_states.Q2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_user_contact, state=Main_states.Q2_1, content_types=["contact"])
    dp.register_message_handler(user_phone_serves_text, state=Main_states.Q2_1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(serves_sto, state=Main_states.Q2_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_date_serves, state=Main_states.Q2_3, content_types=types.ContentTypes.ANY)