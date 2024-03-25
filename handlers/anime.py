import asyncio
from db import connect_to_db

async def populate_anime(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO anime (title, description) VALUES 
        ('Город, в котором меня нет', 'Описание аниме "Сатору обычный 29-летний парень. Работает в пиццерии, мечтает стать мангакой."'),
        ('Ванпанчмен', 'Описание аниме "В мире все чаще появляются разнообразные суперзлодеи, но против них всегда готова выступить Ассоциация героев, так что, человечество почти в безопасности."'),
        ('Форма голоса', 'Описание аниме "Глухая от рождения Секо Нисимия была брошена родным отцом, когда он узнал о неизлечимом недуге дочери."'),
        ('Повелитель', 'Описание аниме "До недавнего времени DMMO-RPG Иггдрасиль была самой популярной игрой на азиатском рынке."')
        """)

async def main():
    pool = await connect_to_db("postgresql://username:password@localhost/database_name")
    await populate_anime(pool)

if __name__ == "__main__":
    asyncio.run(main())
