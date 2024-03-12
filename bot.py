from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN = '6571439480:AAH3ennZ2JxzD5dia3jC-2On1vL2Niirg3k'"))
dp = Dispatcher()