from aiogram import Dispatcher
from aiogram.types import Message

async def message_get_commands(message: Message):
    no_lang = await message.bot.get_my_commands()