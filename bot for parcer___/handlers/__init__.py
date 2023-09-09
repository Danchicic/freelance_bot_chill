from aiogram import Router
from .handlers import just_router
main_router = Router()
main_router.include_router(just_router)