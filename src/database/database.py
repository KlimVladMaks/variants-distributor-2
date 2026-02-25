from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .models import Base

"""
# Работа с сессией БД:

async with AsyncSession() as session:
    # работа с БД
    await session.commit()
"""

async_engine = create_async_engine('sqlite+aiosqlite:///database.db')
AsyncSession = async_sessionmaker(async_engine)

async def init_db() -> None:
    """
    Функция для инициализации таблиц в БД
    (если таблицы уже есть, то ничего не происходит)
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
