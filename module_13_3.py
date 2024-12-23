from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Я', 'учусь'])
async def s_message(message):
    print("message")


@dp.message_handler(commands=['start'])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.TEST")
    await message.answer("Рады вас видеть в нашем боте")


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.TEST2")
    await message.answer(message.text)
    print(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
