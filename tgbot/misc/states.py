from aiogram.dispatcher.filters.state import StatesGroup, State


class Main_states(StatesGroup):

    """Состояния для работы со сценарием Запчасти"""

    Q1=State()
    Q1_1=State()
    Q1_2 = State()
    Q1_3 = State()

    """Состояния для работы со сценарием Сервис"""

    Q2=State()
    Q2_1= State()
    Q2_2= State()
    Q2_3= State()
    Q2_4= State()


    """Состояния для работы со сценарием Кузовной сервис"""

    Q3 = State()
    Q3_1 = State()
    Q3_2 = State()
    Q3_3 = State()

    """Состояния для работы со сценарием Автостраховки"""

    Q4=State()
    Q4_1=State()
    Q4_2=State()
    Q4_3=State()
    Q4_4=State()
    Q4_5=State()
