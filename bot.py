from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Функція для отримання балансу
def get_balance():
    # Тут буде твій код для підключення до RemOnline API
    # Поки що просто повертаємо тестове значення
    return 1000

# Функція, яка викликається на команду /balance
def balance(update: Update, context: CallbackContext):
    balance = get_balance()
    update.message.reply_text(f"Ваш баланс: {balance} грн")

def main():
    # Твій токен бота
    updater = Updater("7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc", use_context=True)


    # Додавання команд
    updater.dispatcher.add_handler(CommandHandler("balance", balance))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
