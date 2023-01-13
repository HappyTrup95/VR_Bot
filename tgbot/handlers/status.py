from cgitb import text
import requests
from distutils.command.config import config
from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext


from tgbot.misc.states import Main_states
from tgbot.keyboards.reply import STO1, last_menu





async def serves_sto(message: types.Message, state: any):
    text = [
        "Выберите СТО",
    ]
    await message.answer('\n'.join(text),reply_markup=STO1.sto)
    await Main_states.Q6.set()

async def number_reg(message: types.Message, state: FSMContext):
    text = [
        "Введите госномер автомобиля и ваш контактный номер телефона\n Пример a123aa +790299911111",
    ]
    await message.answer('\n'.join(text),reply_markup=types.ReplyKeyboardRemove())
    await Main_states.Q6_1.set()

async def state_end(message: types.Message, state: FSMContext):
    text = [
        "Благодарю, мастер-приемщик свяжется с Вами в ближайшее время",
    ]
    await message.answer('\n'.join(text),reply_markup=last_menu.choice)
    base_url=f'http://api.telegram.org/bot5183475207:AAHJVgxcqk4ptQz-Iz0Z-rcGcTWXiAxs6mU/sendMessage?chat_id=-770592579&text="Логин пользователя: @{message.chat.username}\n Имя пользователя - {message.chat.first_name}\n Госномер авто - {message.text}\n СТО - Джили\n Причина обращения - Узнать состояние ремонта авто"'
    requests.get(base_url)
    await state.finish()


def register_status(dp: Dispatcher):
    dp.register_message_handler(serves_sto, state="*", text=["Статус ремонта"])
    dp.register_message_handler(number_reg, state=Main_states.Q6, text=["GEELY"])
    dp.register_message_handler(state_end, state=Main_states.Q6_1, content_types=types.ContentTypes.ANY)

