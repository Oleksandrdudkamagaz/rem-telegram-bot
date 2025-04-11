from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

def get_balance():
    API_KEY = "ffdcb6e1038f410f9c56e234925e5940"  # Замінити на правильний ключ
    url = "https://api.remonline.com/v1/accounts/balance"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("balance", 0)
    except requests.exceptions.RequestException as e:
        print(f"Помилка при запиті до API: {e}")
        return 0

async def balance(update: Update, context: CallbackContext):
    balance = get_balance()
    await update.message.reply_text(f"Ваш баланс: {balance} грн")

def
