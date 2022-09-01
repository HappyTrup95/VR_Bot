from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import Main_menu, User_data_menu, New_user_menu
from tgbot.bd_bot.sql import  insert_data, view_data_id, view_data_phone, view_data_name
from tgbot.misc.states import Main_states

user_name=""
ser_phone=""


async def user_start(message: Message, state: any):
    await message.answer(text = "🤖 Выберите услугу из предложенных ниже. Если что-то пойдет не так — зовите оператора.", reply_markup=Main_menu.main_choice)
    await state.finish()

async def message_get_commands(message: Message, state: any):
    no_lang = await message.bot.get_my_commands()
    id = view_data_id(message.from_user.id)
    if id == message.from_user.id:
        user_name= view_data_name(message.from_user.id)
        ser_phone=view_data_phone(message.from_user.id)
        await message.reply(

            f" Ваше имя - {user_name} \n"
            f" Ваш телефон - {ser_phone} \n"
            " Меняем или оставляем как есть?" , reply_markup= User_data_menu.choice
        )
        await Main_states.Q5.set()
    else:
        await message.reply(

            " У нас нет ваших данных. Хотите заполнить?",reply_markup=New_user_menu.choice

        )
        await Main_states.Q5.set()

async def message_get_commands_operator(message: Message, state: any):
    no_lang = await message.bot.get_my_commands()


    await message.reply(" Для связи с оператором перейдите t.me/VolgaRast_help_bot \n")
    await state.finish()



def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, state="*", commands=["start"])
    dp.register_message_handler(user_start, state="*", text=["Выбрать услугу"])
    dp.register_message_handler(user_start, state="*", text=["Нет, позже"])
    dp.register_message_handler(user_start, state="*", text=["Оставляем"])
    dp.register_message_handler(message_get_commands, state="*", commands=["regist"] )
    dp.register_message_handler(message_get_commands_operator, state="*", commands=["operator"] )
    dp.register_message_handler(message_get_commands_operator, state="*", text=["Позвать оператора"] )  
  
    

