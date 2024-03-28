from aiogram import Router, types
from aiogram.filters import Command
import logging
from db import connect_to_db, get_genres, get_anime_by_genre

genre_router = Router()

async def show_genres(message: types.Message):
    pool = await connect_to_db("YOUR_DATABASE_URL")
    genres = await get_genres(pool)
    kb = types.InlineKeyboardMarkup()
    for genre in genres:
        kb.add(types.InlineKeyboardButton(text=genre['name'], callback_data=f'genre_{genre["id"]}'))
    await message.answer("Выберите жанр аниме:", reply_markup=kb)

@genre_router.callback_query(lambda c: c.data.startswith('genre_'))
async def list_anime(callback: types.CallbackQuery):
    genre_id = callback.data.split('_')[1]
    pool = await connect_to_db("postgresql://username:password@localhost:5432/database_name")
    anime_list = await get_anime_by_genre(pool, int(genre_id))
    response = '\n'.join([f"{anime['title']}: {anime['description']}" for anime in anime_list])
    await callback.message.answer(response)


genre_router = Router()

@genre_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Action", callback_data="action"),
                types.InlineKeyboardButton(text="Comedy", callback_data="comedy")
            ],
            [
                types.InlineKeyboardButton(text="Fantasy", callback_data="fantasy"),
                types.InlineKeyboardButton(text="Drama", callback_data="drama")
            ],
            [
                types.InlineKeyboardButton(text="Adventure", callback_data="adventure"),
                types.InlineKeyboardButton(text="Romance", callback_data="romance")
            ]
        ]
    )

    logging.info(message.from_user)
    await message.answer("Выберите жанр аниме:", reply_markup=kb)

@genre_router.callback_query(F.data == "action")
async def action_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Action")

@genre_router.callback_query(F.data == "comedy")
async def comedy_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Comedy")

@genre_router.callback_query(F.data == "fantasy")
async def fantasy_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Fantasy")

@genre_router.callback_query(F.data == "drama")
async def drama_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Drama")

@genre_router.callback_query(F.data == "adventure")
async def adventure_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Adventure")

@genre_router.callback_query(F.data == "romance")
async def romance_genre(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали жанр Romance")
