
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, PollAnswer
from markup import form_button, menu_button
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu
from main import bot
from random import randint

router=Router()


@router.message(CommandStart())
async def start(message:Message, state:  FSMContext):
    await state.set_state(Form.wait)
    #await bot.send_photo(chat_id= message.chat.id, photo="images/IMG_1608.JPG", caption = "Hey!💘")
    #images = ['images/Иллюстрация_без_названия 9.jpg', 'images/IMG_1608.JPG']
    #await message.answer_photo(photo =FSInputFile(images[randint(0, 1)]))
    await message.answer(text="Hey hey! Заполни анкету", reply_markup=form_button)
    await state.set_state(Form.wait)
    #await message.answer(text="Hey!💘", reply_markup=menu_button)
    #await state.set_state(Menu.to_menu)
    #await message.answer_location(latitude=40.41128727472991, longitude=-3.701609967337579)
#     question = 'Do u listen to David Bowie?'
#     options = ['Yes', 'Yes']
#     await message.answer_poll(question=question, options=options, is_anonymous=False)
#     await message.delete()
#
# @router.poll_answer()
# async def poll_answer(poll_answer:PollAnswer):
#     answer_ids = poll_answer.option_ids
#     print(answer_ids)




