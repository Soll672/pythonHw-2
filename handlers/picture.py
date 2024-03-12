from aiogram import Router, types
from aiogram.filters import Command
from os import listdir, path
import logging
from pathlib import Path


picture_router = Router()


@picture_router.message(Command("pic"))
async def send_pic(message: types.Message):
    # file_name = listdir("images")
    # file_path = path.join("images", file_name)

    files_list = list((Path(__file__).parent.parent/"images").iterdir())

    file_path = files_list[0]
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file, caption="Котик")
    await message.reply("Котик")
