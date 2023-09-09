from aiogram import Router
from aiogram.filters import StateFilter

from aiogram.types import Message

from aiogram.fsm.context import FSMContext

just_router: Router = Router()


@just_router.message(lambda x: "/inn" in x)
async def send_statistic_using_inn(message: Message):
    pass


@just_router.message(lambda x: x.split()[1][:2].isdigit())
async def send_statistic_using_name_and_birthday(message: Message):
    pass
