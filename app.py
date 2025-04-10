import os
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
REM_API_KEY = os.getenv('REM_API_KEY')

@app.route('/')
def hello():
    return "Hello, world!"

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()

    if 'message' in update:
        chat_id = update['message']['chat']['id']
        message = update['message']['text']

        if message == '/balance':
            balance = get_balance_from_remonline()
            send_message(chat_id, f'Your balance: {balance}')

    return 'OK', 200

def get_balance_from_remonline():
    url = "https://api.remonline.com/v1/client/balance"
    headers = {'Authorization': f'Bearer {REM_API_KEY}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get('balance', 0)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    requests.get(url, params=params)

if __name__ == '__main__':
    app.run(debug=True)
