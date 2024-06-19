# from aiogram import Router
# from aiogram.types import Message
# from markup import link_ref_button, buttons_assist
#
#
# router=Router()
#
#
# @router.message()
# async def reply(message: Message):
#     if message.text.lower() in ["меню", "/меню", "/menu"]:
#         await message.answer(text="Welcome!👀\n В этом боте можно найти референсы для скетч-разминок, туториалы и кисти\n Команды:👇🏻\n /help - помощь\n /about - информация о боте ", reply_markup=buttons_assist)
#
#     if message.text.lower() in ["референсы"]:
#
#         await message.answer (text="<b>Ссылка на доску с референсами</b>\n", reply_markup=link_ref_button, parse_mode= "html" )
#
#     if message.text.lower() in ["идеи для поста"]:
#         await message.answer(text="Выбери тему для поста💭✨🎲\n")
#
#     if message.text.lower() in ["туториалы"]:
#         await message.answer(text="Ссылка на папку с туториалами\n")
#
#     if message.text.lower() in ["кисти"]:
#         await message.answer(text="Ссылка на папку с кистями\n")