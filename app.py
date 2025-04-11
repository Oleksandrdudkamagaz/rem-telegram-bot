import requests

API_KEY = "ffdcb6e1038f410f9c56e234925e5940"  # Ваш ключ API

def get_balance():
    url = "https://api.remonline.com/v1/accounts/balance"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)  # Додамо виведення даних для перевірки
        return data.get("balance", 0)
    except requests.exceptions.RequestException as e:
        print(f"Помилка при запиті до API: {e}")
        return 0


# Функція для обробки команди /balance
async def balance(update: Update, context):
    balance = get_balance()
    await update.message.reply_text(f"Ваш баланс: {balance} грн")

def main():
    # Створення додатку
    application = Application.builder().token("8157954971:AAGx0JcArobM0vb7SzZSCiGiEIwL6yrHsQk").build()  # Замініть на ваш токен

    # Додавання обробника для команди /balance
    application.add_handler(CommandHandler("balance", balance))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
