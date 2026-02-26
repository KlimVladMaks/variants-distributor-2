from aiogram.fsm.state import State, StatesGroup


class Common(StatesGroup):
    """Общие состояния (используются до выбора пользователем роли)"""
    pass


class Teacher(StatesGroup):
    """Состояния пользователя с ролью 'Преподаватель'"""
    main_menu_st = State()
