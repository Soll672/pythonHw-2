import asyncpg

async def connect_to_db(database_url):
    return await asyncpg.create_pool(database_url)

async def get_anime_list(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM anime")
