from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import Main_menu


async def user_start(message: Message, state: any):
    await message.answer(text = "Здраствуйте, какая услуга вас интересует?", reply_markup=Main_menu.main_choice)
    await state.finish()

async def message_get_commands(message: Message, state: any):
    no_lang = await message.bot.get_my_commands()


    await message.reply(" Если хотите перейти в начало - /start \n"
    "Если нужна справка нажмите - /help" )
    await state.finish()





def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, state="*", commands=["start"])
    dp.register_message_handler(message_get_commands, state="*", commands=["help"] )
    
    

