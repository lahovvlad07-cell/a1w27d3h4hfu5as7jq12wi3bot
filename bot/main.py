import asyncio
import logging

from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from handlers.start import start

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

async def main_async():
    """Асинхронный вход в приложение."""
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Бот NeonKey запущен!")

    # Инициализация и запуск бота
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # Ожидание завершения (например, по Ctrl+C)
    await app.updater.wait_until_shutdown()

if __name__ == "__main__":
    asyncio.run(main_async())