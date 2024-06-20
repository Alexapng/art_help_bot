from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from markup import link_ref_button
from markup import buttons_assist, ref_button, brush_other_button, ideas_button, chat_button
from random import randint
from states import Menu


router=Router()
data = []

@router.message(Menu.to_menu)
async def reply(message: Message, state: FSMContext):
    if message.text.lower() in ["меню", "/меню", "/menu"]:


        await message.answer(text="Welcome!👀\n\n В этом боте можно найти референсы для скетч-разминок, туториалы и кисти\n\n <b>Команды:</b>👇🏻\n\n /help - помощь\n /about - информация о боте", reply_markup=buttons_assist, parse_mode='html')
        await state.set_state(Menu.menu)
    else:
        await message.answer(text='Переходи в /menu')

@router.message(Menu.menu)
async def reply(message: Message, state: FSMContext):
    if message.text.lower() in ["sketch warm up"]:
        images_1 = ['AgACAgIAAxkBAAICOGZtfZ4wj_ByIySz4fR7z4ejQIlpAAJG2DEbTHRoSxnU6kg_O0anAQADAgADeAADNQQ', 'AgACAgIAAxkBAAICMWZtezrKykFxnu4uu7rDFJkzdv-jAAJB2DEbTHRoS8PsRI9sF7VSAQADAgADeQADNQQ','AgACAgIAAxkBAAICOWZtfdBHEEnaAUE8oEZ8QaEuRHKRAAJN2DEbTHRoS6_sDrukrfSqAQADAgADeAADNQQ','AgACAgIAAxkBAAICRWZtf97P5o_dRIbVW3-PG3JtMGVwAAJY2DEbTHRoS2R3G9ey_lWgAQADAgADeQADNQQ']
        await (message.answer_photo(caption="<b>На один рисунок дается 5-7 минут. Попробуй заскетчить это👆🏻👀</b>\n", photo=images_1[randint(0, 3)],  parse_mode= "html" ))

    if message.text.lower() in ["референсы"]:
        await message.answer(text="Ссылка на доску с референсами\n", reply_markup=ref_button)

    if message.text.lower() in ["кисти"]:
        await message.answer(text="Ссылка на папку с кистями\n", reply_markup=brush_other_button)
        text = '[купить мои кисти](https://boosty.to/alexa_lessons)'
        await message.answer(text=text, parse_mode='MarkdownV2')

    if message.text.lower() in ["сгенерировать идею"]:
        word1 = ['девочка','девушка', 'старушка', 'мальчик', 'кот', 'пес']
        word2 = ['ведьма', 'космонавт', 'пришелец', 'геймер', 'любитель поспать', 'в криповатой тематике', 'y2k', 'рокер', 'мечтатель', 'косплеит твоего любимого персонажа', 'киборг']
        await message.answer(text=" Бот выдаст 2 рандомных слова🤔💭, попробуй создать рисунок на заданную тему✏\n")
        await message.answer(text=f"{word1[randint(0,5)]}-{word2[randint(0,10)]}")

    if message.text.lower() in ["идеи для поста"]:
        await state.set_state(Menu.post_ideas)
        await message.answer(text="Выбери тему для поста💭✨🎲\n", reply_markup=ideas_button)

    if message.text.lower() == "заполнить анкету":
        await  message.answer(text="Введите имя и фамилию")
    else:
        data.append((message.text))


@router.message(Menu.post_ideas)
async def post_ideas_func(message: Message, state: FSMContext):
    if message.text.lower() in ["gm пост"]:
        gm = [' Rise and shine, NFT pioneers! Wishing you a day full of innovation and progress', 'Hey, hey, hey! Wishing you a happy morning and a successful day, NFTcommunity', " Hello, my generous friend! Let's make this day a day of giving back to those in need and spreading kindness"]
        await message.answer(text="Шаблон поста. Просто скопируй его\n\n")
        await message.answer(gm[randint(0,2)])

    if message.text.lower() in ["gn пост"]:
        gn = ["It was a beautiful day. Have a great evening.", 'Sleep tight, my talented friend! May you wake up feeling refreshed and energized in the morning.', "Sweet dreams! Let your creativity run wild and free in your subconscious"]
        await message.answer(text="Шаблон поста. Просто скопируй его\n\n")
        await message.answer(gn[randint(0,2)])

    if message.text.lower() in ["рассуждения"]:
        discussions = ["Напиши 3 варианта поста для Твиттера на английском языке о томчто художнику важно заниматься самообразованием и попроси других художников порекомендовать книги для художников"," Напиши 3 варианта поста для Твиттера на английском языке о томкак интересно художникам узнавать друг друга и предлагаешь другим художникам узнать вас получше и рассказываешь факты о себе такие как.. /здесь добавляйте факты о себе, например я люблю рисовать девушек, меня вдохновляют горы и т.д.", "Напиши 3 варианта поста для Твиттера на английском языке о томкак просишь художников поделиться их любимыми персонажами из фильмов, которых они рисовали"]
        await message.answer(text="Скопируй  шаблон и вставь его в chatgpt\n\n")
        await message.answer(discussions[randint(0, 2)], reply_markup=chat_button)



    if message.text.lower() in ["shill"]:
        discussions = ["Напиши 3 варианта поста для твитера на английском языке о том,что у меня есть планы на продолжение моей коллекции Название коллекции. Я планирую добавить как минимум еще количество невероятных артов. Я безумно люблю эту коллекцию, она значит для меня так много, потому что я вложила в нее свою душу и сердце. Сейчас в этой коллекции доступно количество артов. Предложи посмотреть коллекцию по ссылке в комментариях и при желании каждый может стать владельцем одного из артов"," Напиши 3 варианта поста для твитера на английском языке о том,что моя коллекция состоит из 'количество артов', продаж в этой коллекции - количество продаж, floor price цена ETH, total volume - ваш обьем продаж ETH, счастливых коллекционеров - количество коллекционеров и что ссылка на коллекцию находится в комментариях и что все желающие могут в любой момент стать владельцем арта из этой коллекции"]
        await message.answer(text="Скопируй  шаблон и вставь его в chatgpt\n\n")
        await message.answer(discussions[randint(0, 1)], reply_markup=chat_button)




    if message.text.lower() in ["бросить кубик"]:
        dice = await message.answer_dice()
        print(dice.dice.value)
