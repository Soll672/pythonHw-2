from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from aiogram import types

from scraper import fetch_anime_links

@dp.message_handler(commands=['fetch_anime'])
async def handle_fetch_anime_command(message: types.Message):
    links = await fetch_anime_links()
    if links:
        for link in links:
            await message.answer(link)
    else:
        await message.answer("Не удалось найти аниме.")


async def register_handlers(dp):
    @dp.message_handler(commands=['fetch_anime'])
    async def handle_fetch_anime_command(message: types.Message):
        links = await fetch_anime_links()
        for link in links:
            await message.answer(link)



load_dotenv()
bot_token = os.getenv("6571439480:AAH3ennZ2JxzD5dia3jC-2On1vL2Niirg3k")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
