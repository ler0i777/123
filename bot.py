import json
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Путь к файлу, где будем хранить подписчиков
SUBSCRIBERS_FILE = 'subscribers.json'


def load_subscribers():
    """Загружает подписчиков из файла."""
    try:
        with open(SUBSCRIBERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_subscribers(subscribers):
    """Сохраняет подписчиков в файл."""
    with open(SUBSCRIBERS_FILE, 'w') as file:
        json.dump(subscribers, file)


def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при команде /start."""
    update.message.reply_text('Привет! Используйте команду /subscribe, чтобы подписаться на рассылку.')


def subscribe(update: Update, context: CallbackContext) -> None:
    """Подписывает пользователя на рассылку."""
    user_id = update.message.chat_id
    subscribers = load_subscribers()

    if user_id not in subscribers:
        subscribers.append(user_id)
        save_subscribers(subscribers)
        update.message.reply_text('Вы успешно подписаны на рассылку!')
    else:
        update.message.reply_text('Вы уже подписаны на рассылку.')


def unsubscribe(update: Update, context: CallbackContext) -> None:
    """Отписывает пользователя от рассылки."""
    user_id = update.message.chat_id
    subscribers = load_subscribers()

    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscribers(subscribers)
        update.message.reply_text('Вы успешно отписаны от рассылки.')
    else:
        update.message.reply_text('Вы не были подписаны на рассылку.')


def send_data(context: CallbackContext) -> None:
    """Отправляет данные всем подписчикам."""
    subscribers = load_subscribers()
    for user_id in subscribers:
        context.bot.send_message(chat_id=user_id, text='Вот ваши данные!')


def main() -> None:
    """Запускает бота."""
    # Вставьте сюда токен вашего бота
    token = '7018519797:AAGp13nvCE_6Vcxyer98LVtEgsy-efZ623M'
    updater = Updater(token)

    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))
    dispatcher.add_handler(CommandHandler("unsubscribe", unsubscribe))