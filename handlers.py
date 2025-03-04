from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from config import reply_keyboard

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Вас вітає наш телеграм бот. Виберіть, що вас цікавить.',
        reply_markup=markup
    )

async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_choice = update.message.text

    # Перевіряємо вибір користувача
    if user_choice == 'Отримати квитанцію':
        await update.message.reply_text('Дана функція поки не доступна.', reply_markup=markup)
        return  # Завершуємо функцію, оскільки немає подальших дій для цього вибору

    if user_choice == 'Дізнатися борг':
        await update.message.reply_text('Будь ласка, введіть вашу адресу:')
        context.user_data['choice'] = user_choice
        return

    # Обробка адреси після вибору "Дізнатися борг"
    address = update.message.text
    choice = context.user_data.get('choice', '')

    if 'борг' in choice:
        response = f'Борг для адреси {address}: [дані про борг]'
    else:
        response = 'Невідома команда.'

    await update.message.reply_text(response, reply_markup=markup)

