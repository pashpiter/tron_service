from database.connection import async_engine

from models.wallet import Base


async def create_table() -> None:
    '''Создание таблицы'''
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
