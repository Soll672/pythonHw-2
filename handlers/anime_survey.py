from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class AnimeSurveyStates(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()


anime_survey_router = Dispatcher()

@anime_survey_router.message(commands=['start'])
async def start_anime_survey(message: types.Message):
    await message.answer("Привет! Давай узнаем немного о твоих предпочтениях в аниме.")

    await message.answer("Самое первое аниме, которое вы смотрели?")
    await AnimeSurveyStates.Q1.set()

@anime_survey_router.message(state=AnimeSurveyStates.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    first_anime = message.text.strip()
    if not first_anime:
        await message.answer("Пожалуйста, введите название аниме.")
        return
    await state.update_data(first_anime=first_anime)

    await message.answer("Когда вы подсели на аниме?")
    await AnimeSurveyStates.Q2.set()

@anime_survey_router.message(state=AnimeSurveyStates.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    when_started = message.text.strip()
    if not when_started:
        await message.answer("Пожалуйста, введите дату или описание.")
        return
    await state.update_data(when_started=when_started)

    await message.answer("Любимый персонаж аниме?")
    await AnimeSurveyStates.Q3.set()

@anime_survey_router.message(state=AnimeSurveyStates.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    favorite_character = message.text.strip()
    if not favorite_character:
        await message.answer("Пожалуйста, введите имя персонажа.")
        return
    await state.update_data(favorite_character=favorite_character)

    await message.answer("Нелюбимый персонаж аниме?")
    await AnimeSurveyStates.Q4.set()

@anime_survey_router.message(state=AnimeSurveyStates.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    least_favorite_character = message.text.strip()
    if not least_favorite_character:
        await message.answer("Пожалуйста, введите имя персонажа.")
        return
    await state.update_data(least_favorite_character=least_favorite_character)

    user_data = await state.get_data()
    await message.answer(f"Спасибо за ответы!\n\n"
                         f"Самое первое аниме: {user_data['first_anime']}\n"
                         f"Когда подсели на аниме: {user_data['when_started']}\n"
                         f"Любимый персонаж аниме: {user_data['favorite_character']}\n"
                         f"Нелюбимый персонаж аниме: {user_data['least_favorite_character']}")
    await state.finish()
