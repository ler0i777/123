import logging
from aiogram import Bot, Dispatcher, executor, types

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен вашего бота
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# URL-адрес страницы, которую будет отправлять бот
PAGE_URL = 'https://example.com/page'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Используйте команду /subscribe, чтобы подписаться и получить ссылку на страницу.")

# Обработчик команды /subscribe
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    await message.reply(f"Спасибо за подписку! Вот ваша ссылка на страницу: {PAGE_URL}")

def main():
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
