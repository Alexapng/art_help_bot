from aiogram.filters import Command
from aiogram.types import Message
from markup import links_button
from aiogram import Router

router=Router()


@router.message(Command("about"))
async def about(message:Message):
    text = "Бот, который может сгенерировать идею для рисунка, подобрать референсы и нйати крутые кисти🌚"
    await message.answer(text=text, reply_markup=links_button)
    await message.delete()