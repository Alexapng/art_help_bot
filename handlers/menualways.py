from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from markup import buttons_assist

router=Router()

@router.message(Command("menu"))
async def menu(message:Message):
    await message.answer(text='Welcome!👀\n\n В этом боте можно найти референсы для скетч-разминок, туториалы и кисти\n\n <b>Команды:</b>👇🏻\n\n /help - помощь\n /about - информация о боте',  parse_mode= "html", reply_markup=buttons_assist)


