from sqlalchemy import select

from .database import AsyncSession
from .models import Teacher


async def is_teacher_chat_id(chat_id: int) -> bool:
    """
    Проверяет, принадлежит ли данный chat_id преподавателю.
    Если да, то возвращает True, иначе - False
    """
    async with AsyncSession() as session:
        teacher = await session.execute(
            select(Teacher)
            .where(Teacher.chat_id == chat_id)
        )
        teacher = teacher.scalar_one_or_none()
        return True if teacher else False





