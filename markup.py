from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="меню")]
    ]
    )

buttons_assist = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sketch warm up")],
        [KeyboardButton(text="Референсы")],
        [KeyboardButton(text="Кисти")],
        [KeyboardButton(text="Сгенерировать идею")],
        [KeyboardButton(text="Идеи для поста")]
    ]
)

links_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='инст',
                              url='https://www.instagram.com/_alexa.png_?igsh=NHpzYzBvYjZmaGt2&utm_source=qr')],
        [InlineKeyboardButton(text="pinterest🌼", url='https://pin.it/5dBucOYfX')],
        [InlineKeyboardButton(text='tg🐄', url='https://t.me/Alexa_png')]
    ]
)

link_ref_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Попробуй заскетчить что-то из этого за 5-7 минут')]
    ]
)

form_button= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="заполнить анкету")]
    ]
    )


ref_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ссылка на доску с референсами', url='https://pin.it/36Dzp8Ig5')]
    ]
)

brush_other_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ссылка на кисти для ibis paint', url='https://pin.it/36Dzp8Ig5')],
        [InlineKeyboardButton(text='Ссылка на кисти для Procreate', url='https://pin.it/36Dzp8Ig5')]
    ]
)





ideas_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="GM пост")],
        [KeyboardButton(text="GN пост")],
        [KeyboardButton(text="Рассуждения")],
        [KeyboardButton(text="Shill")]
    ]
)


chat_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Копируй текст и переходи в ChatGPT', url='https://t.me/ChatGPT_General_Bot')]
    ]
)