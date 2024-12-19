from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! ✋\n"
        "Это поддержка Антидетект браузера Multiaccount.\n\n"
        "Мы онлайн и готовы помочь. Задайте свой вопрос!"
    )

# Основной код для запуска бота
TOKEN = "7352937080:AAE3efQNcg9oigyTrYd7_UuXeMto774b2zI"

if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавление обработчика команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()
