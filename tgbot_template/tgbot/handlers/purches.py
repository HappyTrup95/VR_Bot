from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.types import BotCommandScopeChat
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.reply import User_phone
from tgbot.misc.states import Main_states

pur_phon = ""
async def purches(message: types.Message, state: None):
    text = [
        "Укажите свой номер телефона в формате +7999999999",
        "Или поделитесь"
    ]
    await message.answer('\n'.join(text), reply_markup= User_phone.phone)
    await Main_states.Q1.set()


async def user_contact(message: Message, state: FSMContext):
    await message.answer(text = "Напишите название запчасти или артикул запчасти")
    phone_name = message.contact.phone_number
    await Main_states.Q1_1.set()

async def user_contact_text(message: Message, state: FSMContext):
    try:
        pur_phon = message.text.find('+7')
    except:
        pur_phon=-1
    if pur_phon != -1:
        await message.answer(text = "Напишите название запчасти или артикул запчасти")
        await Main_states.Q1_1.set()
    else:
        await message.answer(text = "Неверная команда, попробуйте снова")


async def name_purches(message: Message, state: FSMContext):
    await message.answer(text = "Для подбора автозапчасти необходим VIN номер автомобиля. Введите пожайлуста.")
    await Main_states.Q1_2.set()

async def purches_end(message: Message, state: FSMContext):
    await message.answer(text = "Наш специалист проверит наличие или возможность заказа запчасти и связжеться с Вами.\n Для возврата нажмите /start")
    await state.finish()


def register_purches(dp: Dispatcher):
    dp.register_message_handler(purches, text=["Подбор запчастей"])
    dp.register_message_handler(user_contact, state=Main_states.Q1, content_types=["contact"])
    dp.register_message_handler(user_contact_text, state=Main_states.Q1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(name_purches, state=Main_states.Q1_1, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(purches_end, state=Main_states.Q1_2, content_types=types.ContentTypes.ANY)