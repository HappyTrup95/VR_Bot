from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import User_phone,Choice_user_yes, last_menu
from tgbot.bd_bot.sql import  insert_data, view_data_id, update_data
from tgbot.misc.states import Main_states


user_phone = []
user_name = []

async def registr_start(message: Message, state: FSMContext):
        text = [
            "Укажите свой номер телефона в формате +7999999999",
            "Или поделитесь"
        ]
        await message.answer('\n'.join(text), reply_markup=User_phone.phone )

async def reregistr_name(message: Message, state: FSMContext):
    await message.answer(text = f"Ваше имя - {message.from_user.first_name}\n Если это так нажмите кнопку да\n Иначе напишите его",reply_markup= Choice_user_yes.user_choice)
    await Main_states.Q5_1.set()

async def user_phone_serves_text(message: types.Message, state: FSMContext):
    try:
        ser_phon1 = ""
        ser_phon1 = message.text.find('+7')        
    except:
        ser_phon1=-1
    if ser_phon1 != -1:
        await message.answer(text = f"Ваше имя - {message.from_user.first_name}\n Если это так нажмите кнопку да\n Иначе напишите его",reply_markup= Choice_user_yes.user_choice)
        await Main_states.Q5_1.set()
        user_phone.append(message.text) 
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")

async def regist_last(message: types.Message, state: FSMContext):
    await message.answer(text = "Данные сохранены!", reply_markup=last_menu.choice)
    if message.text == "Да":
        user_name.append(message.from_user.first_name)
    else:
        user_name.append(message.text)
    await state.finish()
    id = view_data_id(message.from_user.id)
    if id == message.from_user.id:
        update_data(message.from_user.id, user_name[0],user_phone[0])
    else:
        insert_data(message.from_user.id, user_name[0],user_phone[0])

def register_user_change(dp: Dispatcher):
    dp.register_message_handler(registr_start, state=Main_states.Q5, text=["Перезаполнить"])
    dp.register_message_handler(registr_start, state=Main_states.Q5, text=["Заполнить"])
    dp.register_message_handler(reregistr_name, state=Main_states.Q5,content_types=["contact"])
    dp.register_message_handler(user_phone_serves_text, state=Main_states.Q5, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(regist_last, state=Main_states.Q5_1, content_types=types.ContentTypes.ANY)