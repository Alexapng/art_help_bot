from aiogram.filters import CommandStart
from re import fullmatch
from aiogram.types import Message
from markup import form_button, buttons_assist
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu
from database import create_profile, edit_profile

router = Router()



@router.message(Form.wait)
async def waiting(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == 'заполнить анкету':
        await state.set_state(Form.name)
        text = "Введите имя"
        await message.answer(text=text)
    else:
        text = "Я тебя не понимаю, нажми на кнопку ниже, чтобы начать заполнять анкету"
        await message.answer(text=text)

@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        text = " отлично, введите возраст"
        await message.answer(text=text)
    else:
        text = "введите корректное имя"
        await message.answer(text=text)


@router.message(Form.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.set_state(Form.email)
        await state.update_data(age=message.text)
        text = " отлично, введите email"
        await message.answer(text=text)
    else:
        text = "введите корректный возраст"
        await message.answer(text=text)



@router.message(Form.email)
async def email(message: Message, state: FSMContext):
    if fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)", message.text):
        await state.set_state(Menu.to_menu)
        await state.update_data(mail=message.text)
        data_dict = await state.get_data()
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'], data_dict['name'], data_dict['age'], data_dict['mail'])
        text = " отлично, переходи в меню /menu"
        await message.answer(text=text, reply_markup=buttons_assist)
    else:
        text = "введите корректный email"
        await message.answer(text=text)
#         await state.set_state(Form.stop)

#
# @router.message(Form.stop)
# async def stop(message:Message,state:FSMContext):
#     pass