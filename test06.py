
from aiogram import Dispatcher, executor, Bot, types
from modules import echo_handler, admin_module

bot_token = '7941202954:AAHxROKXFx0Rrp9N4R0EFUdTvwFUOp9Q3LI'  # Замените на ваш токен
bot = Bot(token=bot_token)

dp = Dispatcher(bot)

echo_module.register_handlers(dp)
admin_module.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp)

