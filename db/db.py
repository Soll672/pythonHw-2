import asyncio


async def connect_to_db(database_url):
    return await asyncpg.create_pool(database_url)

async def get_anime_list(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM anime")

async def main():
    database_url = "postgresql://username:password@localhost:5432/database_name"
    pool = await connect_to_db(database_url)
    anime_list = await get_anime_list(pool)
    for anime in anime_list:
        print(anime)


async def populate_anime(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO anime (title, description) VALUES 
        ('Город, в котором меня нет', 'Описание аниме "Сатору обычный 29-летний парень. Работает в пиццерии, мечтает стать мангакой."'),
        ('Ванпанчмен', 'Описание аниме "В мире все чаще появляются разнообразные суперзлодеи, но против них всегда готова выступить Ассоциация героев, так что, человечество почти в безопасности."'),
        ('Форма голоса', 'Описание аниме "Глухая от рождения Секо Нисимия была брошена родным отцом, когда он узнал о неизлечимом недуге дочери."'),
        ('Повелитель', 'Описание аниме "До недавнего времени DMMO-RPG Иггдрасиль была самой популярной игрой на азиатском рынке."')
        """)



if __name__ == "__main__":
    asyncio.run(main())