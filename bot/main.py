import asyncio
import logging

from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from handlers.start import start

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Явно создаём цикл событий (необходимо для Python 3.14+)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Удаляем вебхук и сбрасываем очередь перед запуском
    loop.run_until_complete(app.bot.delete_webhook(drop_pending_updates=True))

    print("✅ Бот NeonKey запущен!")
    # Запускаем polling с очисткой обновлений
    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=None
    )

if __name__ == "__main__":
    main()
