import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import main_router

# Инициализируем логгер
logger = logging.getLogger(__name__)

TOKEN = "6409412666:AAF-sOG7BToyG1L-mEd6TVuQEDTsBlGnSj0"


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=TOKEN,
                   parse_mode='HTML',
                   )

    dp: Dispatcher = Dispatcher()

    dp.include_router(main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
