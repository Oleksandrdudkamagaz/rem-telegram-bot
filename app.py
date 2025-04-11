import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Твій API-ключ RemOnline
API_KEY = "ffdcb6e1038f410f9c56e234925e5940"

# Функція для отримання балансу через API RemOnline
def get_balance():
    url = "https://api.remonline.com/v1/accounts/balance"  # Заміни на реальний URL API RemOnline (якщо він відрізняється)
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # Передаємо API-ключ у заголовку
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Перевіряє, чи немає помилок у відповіді
        data = response.json()  # Отримуємо JSON-дані з відповіді
        
        # Припускаємо, що відповідь має вигляд:
        # { "balance": 1000 }
        return data.get("balance", 0)  # Повертаємо баланс або 0, якщо не знайдено
    except requests.exceptions.RequestException as e:
        print(f"Помилка при запиті до API: {e}")
        return 0

# Функція, яка викликається на команду /balance
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    balance = get_balance()  # Викликаємо функцію для отримання балансу
    await update.message.reply_text(f"Ваш баланс: {balance} грн")

def main() -> None:
    """Запуск бота."""
    # Твій токен бота
    application = Application.builder().token("7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc").build()

    # Додавання команд до бота
    application.add_handler(CommandHandler("balance", balance))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
