import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import tests


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(tests.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
