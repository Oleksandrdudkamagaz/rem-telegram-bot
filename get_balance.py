import requests

# Замість 'ваш_API_ключ' вставте ваш реальний API ключ
REM_ONLINE_API_KEY = 'ваш_API_ключ'

# Вкажіть ID клієнта, баланс якого ви хочете отримати
client_id = 'ID_клієнта'

# Формуємо URL для запиту
url = f'https://api.remonline.com/v1/clients/{client_id}/balance'

# Встановлюємо заголовок з API ключем
headers = {
    'Authorization': f'Bearer {REM_ONLINE_API_KEY}'
}

# Виконуємо запит до API
response = requests.get(url, headers=headers)

# Перевіряємо статус код відповіді
if response.status_code == 200:
    data = response.json()
    print(f"Баланс клієнта: {data['balance']}")
else:
    print(f"Помилка запиту: {response.status_code}")
