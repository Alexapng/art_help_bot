import asyncio
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
import command_handler, waiting
from config_reader import config
import menu
from handlers import about, help, start, menualways
from anti_spam import AntiFloodMiddleWare

from database import start_db


# bot = Bot(config.bot_token.get_secret_value())
bot = Bot('7489483282:AAFqroR907a6KJggIi_wzA7_ikwyFHta6dw')
dp = Dispatcher()




async def main():
    await start_db()
    dp.message.middleware(AntiFloodMiddleWare())
    dp.include_routers(
        menualways.router,
        start.router,
        about.router,
        waiting.router,
        help.router,
        command_handler.router,
    )
    await dp.start_polling(bot)
if __name__ =="__main__":
    asyncio.run(main())
