import asyncio
import logging

from bot import bot, dp
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.echo import echo_router
from handlers.anime_survey import anime_survey_router

async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(anime_survey_router)

    # в самом конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())