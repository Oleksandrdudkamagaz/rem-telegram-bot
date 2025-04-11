from telegram import Update
from telegram.ext import Application, CommandHandler

# Обробник для команди /start
async def start(update: Update, context):
    await update.message.reply_text('Hello! I\'m your bot.')

# Основна функція
async def main():
    # Ваш токен
    token = "7775775049:AAEWIkhx2zhYOk23EJQO8nRHHQ6a_hBl6Rc"
    
    # Створюємо об'єкт Application
    application = Application.builder().token(token).build()

    # Додаємо обробник для команди /start
    application.add_handler(CommandHandler("start", start))

    # Запускаємо бота
    await application.run_polling()

# Запуск бота
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
