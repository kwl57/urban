'''Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку
 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и
'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(level=logging.INFO)
api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# ------ Марк ап клавиатура (с кнопками)----------------
kb = ReplyKeyboardMarkup(resize_keyboard=True) # инициализация клавиатуры
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.row(button)
kb.row(button2)

#-------- Ин лайн клавиатура (с кнопками)----------------
kb2 = InlineKeyboardMarkup()
in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(in_button1)
kb2.add(in_button2)
#namefull = 'гость'
# Создание клавиатуры
#kbi = InlineKeyboardMarkup(resize_keyboard=True)
#button = KeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
#button2 = KeyboardButton(text='Формулы расчёта', callback_data='formulas')
#kb.row(button, button2)


#s_m = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='Выберите опцию:')],
#          [
#             KeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
#             KeyboardButton(text='Формулы расчёта', callback_data='formulas')
#         ]
#     ], resize_keyboard=True)



# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Хэндлер команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

# Хэндлер для кнопки "Рассчитать"
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора: '
                                 '(10 * вес + 6.25 * рост - 5 * возраст + 5)')
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
                              '\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')

    await call.answer()
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст: (лет)')
    await call.answer()
    await UserState.age.set()

#Хэндлер для кнопки "Информация"
@dp.message_handler(text='Информация')
async def info_message(message: types.Message):

        await message.answer('Я бот, который помогает рассчитывать калории и следить '
                          'за твоим здоровьем.')
        data_task = {'user_id': message.from_user.id, 'full_name': message.from_user.full_name,
                     'username': message.from_user.username, 'message_id': message.message_id,
                     }
        global namefull
        namefull = data_task.get('full_name')
        print(data_task)
        print(namefull)


# Хэндлер для состояния age
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: (в см)')
    await UserState.growth.set()

# Хэндлер для состояния growth
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: (кг)')
    await UserState.weight.set()

# Хэндлер для состояния weight и расчет калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)


    data = await state.get_data()
    try:
        age = float(data['age'])
        weight = float(data['weight'])
        growth = float(data['growth'])
    except:
        await message.answer(f'Не могу конвертировать введенные значения в числа.')
        await state.finish()
        return

    # Упрощенный вариант формулы Миффлина-Сан Жеора:
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    #для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
    calories_wom = 10 * weight + 6.25 * growth - 5 * age - 161
    result = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Норма (муж.): {calories_man} ккал')
    await message.answer(f'Норма (жен.): {calories_wom} ккал')
    await message.answer(f'Ваша {namefull}  норма калорий: {result} в день.')


    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)