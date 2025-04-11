from telegram import Update
from telegram.ext import CommandHandler, Updater

# Функція для команди /start
def start(update: Update, context):
    update.message.reply_text("Hello! I'm your bot.")

# Функція для команди /balance
def balance(update: Update, context):
    update.message.reply_text("Your balance is $100.")

def main():
    token = "7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc"
    
    # Створення об'єкта Updater
    updater = Updater(token, use_context=False)
    dp = updater.dispatcher

    # Додавання обробників команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("balance", balance))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
