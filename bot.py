from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

def start(update: Update, context):
    update.message.reply_text("Hello! I'm your bot.")

def main():
    token = "7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc"
    updater = Updater(token, use_context=False)  # Важливо встановити use_context=False
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
    # Оновлений код для створення бота:
    application = Application.builder().token("7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc").build()
    
    # Додавання обробника для команди /balance:
    application.add_handler(CommandHandler("balance", balance))
    
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
