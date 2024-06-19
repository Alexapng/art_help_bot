from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

router=Router()


@router.message(Command("help"))
async def help(message:Message):
    await message.answer(text="Hi! Список команд👇🏻👀\n"
                        "/start - запустить бота\n"
                        "/help - показать все команды\n"
                        "/menu - Меню\n"
                         "/about -  информация о боте")
    await message.delete()