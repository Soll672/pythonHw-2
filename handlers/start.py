import asyncio
import logging

from aiogram import Bot, Dispatcher
from bot import bot, dp
from handlers.start import start_router
from handlers.genres import genre_router
from handlers.echo import echo_router


async def main():
    # Регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(genre_router)
    dp.include_router(echo_router)
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


def start_router():
    return None