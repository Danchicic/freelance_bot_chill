from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile, CallbackQuery

from aiogram.types import Message
from lexicon import lexicon
from keyboards import choose_country_kb

just_router: Router = Router()


def birthday_filter(message) -> bool:
    """
    from <Балукова татьяна, 12.11.1987> trying to take only 12
    """
    x = message
    print(x.text)
    return x.text.split(',')[1].strip()[:2].isdigit() if len(x.text.split(',')) != 1 else 0


@just_router.message(Command(commands="start"))
async def hello_message(message: Message):
    await message.answer(text='Два режима: по инн (/inn номер) по имени и дате рождения')


@just_router.message(Command(commands="inn"))
async def send_statistic_using_inn(message: Message):
    await message.reply_document(FSInputFile('handlers/data1.html'))


@just_router.message(birthday_filter)
async def send_statistic_using_name_and_birthday(message: Message):
    await message.answer(text=lexicon['choose_country'], reply_markup=choose_country_kb())


@just_router.callback_query(F.data == 'Россия')
async def send_statistic_using_name_and_birthday(callback: CallbackQuery):
    await callback.message.edit_text(lexicon['birthday_message'])
    await callback.answer()
