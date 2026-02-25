from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..database import crud


router = Router()


@router.message()
async def default_router(message: Message, state: FSMContext):
    chat_id = message.chat.id
    is_teacher = await crud.is_teacher_chat_id(chat_id)
    # if is_teacher:
    #     await message.answer(
    #         "Здравствуйте! Похоже, бот был перезапущен. " \
    #         "Вы будете перенаправлены в главное меню."
    #     )
    #     await state.set_state(TS.main_menu_st)
    #     await teacher_main_menu(message, state, is_init=True)
    #     return
    # student = await crud.get_student_by_chat_id(chat_id)
    # if student:
    #     await message.answer(
    #         f"Здравствуйте, {student.full_name}! Похоже, бот был перезапущен. " \
    #         f"Вы будете перенаправлены в главное меню."
    #     )
    #     await student_main_menu_router(message, state)
    # else:
    #     await state.set_state(CS.choosing_role_st)
    #     await choosing_role(message, state, is_init=True)
