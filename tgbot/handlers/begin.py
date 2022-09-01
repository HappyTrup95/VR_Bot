from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_main_menu(message: types.Message):
    text = [
        "🤖 Привет! Я — робот Волга-Раста.\n Помогу подобрать запчасти, записаться на ремонт и многое другое.\n ",
        "🤖 Выберите услугу из предложенных ниже. Если что-то пойдет не так — зовите оператора."
    ]

    await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_main_menu)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)

