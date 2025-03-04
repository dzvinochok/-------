from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers import start, handle_choice

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_choice))

    application.run_polling()

if __name__ == '__main__':
    main()
