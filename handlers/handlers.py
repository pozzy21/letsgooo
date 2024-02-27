from smtp import send_mail
from aiogram.types import FSInputFile
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards.inline import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiosmtplib import SMTP
import asyncio
from aiogram.utils.formatting import Text, Bold
from bot import delete

time1 = 1800
time2 = 7200
time3 = 86400
mailto = 'pozzy199911@gmail.com'

# subj,to,msg #asyncio.run(send_mail('Тема письма','pozzy199911@gmail.com', '<h1>Привет</h1>'))

router = Router()


@router.message(F.photo)
async def echo_gif(message: Message):
    await message.reply_photo(message.photo.file_id)


class MakeOrder(StatesGroup):
    start_message = State()
    name = State()
    phone = State()
    start_message_2 = State()
    help_state = State()
    help_state_message = State()
    help_state_phoneme = State()  # А потом сброс стейта или чи шо
    start_message_3 = State()  # Тут указывать параметры авто
    model_auto = State()
    date_auto = State()
    kuzov_auto = State()
    additional_info = State()
    type_of = State()
    nashi_covriki = State()
    material_of = State()
    color_of = State()
    color_cover = State()
    color_cant = State()
    dopniki = State()
    pyatka = State()
    shield = State()
    final = State()
    wait30 = State()
    wait120 = State()
    wait1440 = State()
    cantik_color = State()
    nigga = State()

# Это еще не конец блин

# @router.message(F.animation)
# async def echo_gif(message: Message):
#     await message.reply_animation(message.animation.file_id)


@router.message(MakeOrder.start_message)
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Поехали",
        callback_data="poehali"),

    )
    await message.answer(
        text="Привет! С помощью этого сервиса ты можешь быстро\nоформить заявку на коврики Eva Standart в твое авто.\n\n\
Как это работает? \n\n\
Тебе нужно будет заполнить данные в трех блоках:\n\
1. Технические характеристики автомобиля\n\
2. Выбрать цвет ковриков и канта\n\
3. Указать дополнительные параметры\n\n\
Нажми на кнопку ниже, чтобы начать подбор👇\n",
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message)


@router.callback_query(F.data == 'Back_to_start')
async def back2start(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Поехали",
        callback_data="poehali")
    )
    await query.message.answer(
        text="Привет! С помощью этого сервиса ты можешь быстро\n оформить заявку на коврики Eva Standart в твое авто.\n\n\
Как это работает? \n\n\
Тебе нужно будет заполнить данные в трех блоках:\n\n\
1. Технические характеристики автомобиля\n\
2. Выбрать цвет ковриков и канта\n\
3. Указать дополнительные параметры\n\n\
Нажми на кнопку ниже, чтобы начать подбор👇\n",
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message)


@router.message(MakeOrder.start_message)
@router.callback_query(F.data == "poehali")
async def set_name(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        text="Как тебя зовут?"
    )
    await state.set_state(MakeOrder.name)
    current_state = await state.get_state()
#     print(current_state)
#     # Проверить как работает
#     await asyncio.sleep(10)
# # Определять функцию клавы перед хендлером на который навесил
#     if (current_state == await state.get_state()):
#         await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
# Пока ты думал, твой салон стал грязнее\n\
# потратил 3000 на химчистку\n\n\
# Или просто позвони\n\
# +7(914)5-501-502', reply_markup=wait_kb())
#         await asyncio.sleep(10)
#         print('success1')

#         await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
# Нужна помощь в подборе? Звони:\n\
# +7(914)5-501-502', reply_markup=wait_kb())
#         await asyncio.sleep(10)
#         print('success2')
#         await query.message.answer(text='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
# Нужна помощь в подборе? Звони:\n\
# +7(914)5-501-502', reply_markup=wait_kb())


# 4test


@router.message(MakeOrder.name)
async def set_phone(message: Message, state: FSMContext):
    await state.update_data(chosen_name=message.text)
    user_data = await state.get_data()  # по хорошему потом убрать подобное
    await message.answer(
        text="После оформления заказа мы свяжемся с тобой для подтверждения заявки. Для этого укажи свой номер телефона, чтобы не потерять связь с нами👇"
    )
    print(f"Клиент ввел имя {user_data['chosen_name']}")
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.phone)


@router.message(MakeOrder.phone)
async def start_message(message: Message, state: FSMContext):
    await state.update_data(chosen_phone=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Супер! Приступим к подбору",
        callback_data="Super")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back_to_start")
    )

    await message.answer_photo(
        photo='AgACAgIAAxkDAAIGJ2Wp6UXRnAvAcUgHJyZHTvuKSAYPAAL-2jEbE81QSaU-QYFbdbafAQADAgADeQADNAQ',
        caption="<b>У нас собственное четко отлаженное производство ковриков по более чем 1000 лекал для разных марок и моделей авто</b> \n\n\
Для изготовления ковриков мы используем EVA-материал российского производства высокого качества\n\n\
Срок изготовления - 24 часа с момента внесения оплаты (предоплаты) \n\
\n\
Цена зависит от количества материала, в среднем за салон(без багажника) - от 3400 рублей \n",
        reply_markup=start_kb()
    )
    user_data = await state.get_data()
    # по хорошему потом убрать подобное
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message_2)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'pricol')
async def deletemsg(query: CallbackQuery, state: FSMContext):
    await query.message.delete()


@router.callback_query(F.data == 'Back')
async def back(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Супер! Приступим к подбору",
        callback_data="Super")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back_to_start")
    )

    # тут вставить картинку
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIGJ2Wp6UXRnAvAcUgHJyZHTvuKSAYPAAL-2jEbE81QSaU-QYFbdbafAQADAgADeQADNAQ',
        caption="<b>У нас собственное четко отлаженное производство ковриков по более чем 1000 лекал для разных марок и моделей авто</b> \n\n\
Для изготовления ковриков мы используем EVA-материал российского производства высокого качества\n\n\
Срок изготовления - 24 часа с омента внесения оплаты (предоплаты) \n\n\
\n\
Цена зависит от количества материала, в среднем за салон(без багажника) - от 3400 рублей \n",
        reply_markup=start_kb()
    )
    # по хорошему потом убрать подобное
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message_2)
    current_state = await state.get_state()
    print(current_state)
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back")
    )
    await query.message.answer(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'callme')
async def call_me(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(text='Приняли! Перезвоним в ближайшее время 🤝')
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await send_mail('Консультация, звонок', mailto, f"<h1>Контакты клиента:</h1>\n\
Имя: {user_data['chosen_name']} \n\
Телефон: {user_data['chosen_phone']}")
    await state.set_state(MakeOrder.help_state_phoneme)


@router.callback_query(F.data == 'textme')
async def text_me(query: CallbackQuery, state: FSMContext):
    # Отправить email с просьбой написать по номеру телефона(Ватсап получается, или запросить шаринг своего контакта?)
    await query.message.edit_text(text='Отлично, мы свяжемся в ближайшее время!')
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await send_mail('Консультация, написать', mailto, f"<h1>Контакты клиента:</h1>\n\
Имя: {user_data['chosen_name']}\n\
Телефон: {user_data['chosen_phone']}")
    await state.set_state(MakeOrder.help_state_message)


@router.callback_query(F.data == 'Super')
async def order(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Указать параметры моего авто",
        callback_data="auto")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIQKWXWylBOXJKzxlnUpji4C34vIHFSAAJT3DEbLIuxSsIwRZ7jRk7SAQADAgADdwADNAQ',
        caption='Чтобы коврики легли четко, нам нужно знать параметры твоего автомобиля 👌\n\
\n \
В сообщениях ниже укажи параметры своего авто\n\
В любой момент ты сможешь обратиться за консультацией. Для этого нажми кнопку "Мне нужна помощь"',
        reply_markup=order_1_kb()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message_3)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help1')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_0")
    )
    await query.message.answer(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_0')
async def order_b(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Указать параметры моего авто",
        callback_data="auto")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIQKWXWylBOXJKzxlnUpji4C34vIHFSAAJT3DEbLIuxSsIwRZ7jRk7SAQADAgADdwADNAQ',
        caption='Чтобы коврики легли четко, нам нужно знать параметры твоего автомобиля 👌\n\
\n \
В сообщениях ниже укажи параметры своего авто \n \
В любой момент ты сможешь обратиться за консультацией. Для этого нажми кнопку "Мне нужна помощь"',
        reply_markup=order_1_kb()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.start_message_3)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'auto')
@router.message(MakeOrder.start_message_3)
async def order_1(query: CallbackQuery, state: FSMContext):
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIGJWWp6UM28uwOo9kz5jUJjN9EsdMnAAL82jEbE81QSc2wdA-08ssqAQADAgADeQADNAQ',
        caption='Где найти все точные характеристики твоего авто?'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_0")
    )
    await query.message.answer(
        text='<b>Введите марку и модель авто</b>',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.model_auto)


@router.callback_query(F.data == 'help2')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_1")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_1')
async def order_1_b(query: CallbackQuery, state: FSMContext):
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIGJWWp6UM28uwOo9kz5jUJjN9EsdMnAAL82jEbE81QSc2wdA-08ssqAQADAgADeQADNAQ',
        caption='Где найти все точные характеристики твоего авто?'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_0")
    )
    await query.message.answer(
        text='<b>Введите марку и модель авто</b>',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.model_auto)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.model_auto)
async def order_2(message: Message, state: FSMContext):
    await state.update_data(chosen_model=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_1")
    )
    await message.answer_photo(
        photo='AgACAgIAAxkDAAIGImWp6UHlW9YMsuisMJLDzM_ZM_2LAAL52jEbE81QSfQcjrymuf7tAQADAgADeQADNAQ',
        caption="Чтобы долго не искать все параметры, просто открой свид-во о регистрации или загляни в ПТС"
    )
    await message.answer(
        text='<b>Введите год выпуска</b>',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.date_auto)
    current_state = await state.get_state()
    print(current_state)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help2')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_2")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_2')
async def order_2_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_model=query.message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_1")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIGImWp6UHlW9YMsuisMJLDzM_ZM_2LAAL52jEbE81QSfQcjrymuf7tAQADAgADeQADNAQ',
        caption="Чтобы долго не искать все параметры, просто открой свид-во о регистрации или загляни в ПТС"
    )
    await query.message.answer(
        text='<b>Введите год выпуска</b>',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.date_auto)
    current_state = await state.get_state()
    print(current_state)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.date_auto)
async def order_3(message: Message, state: FSMContext):
    await state.update_data(chosen_date=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_2")
    )
    await message.answer_photo(
        photo='AgACAgIAAxkDAAIGI2Wp6UL0G8X7XDFZV_zlJpN0h1JrAAL62jEbE81QSQpAbm4VDCgiAQADAgADeQADNAQ',
        caption="Перепиши номер кузова из свидетельства о регистрации"
    )
    await message.answer(
        text='<b>Укажите какой кузов у авто</b>', reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.kuzov_auto)
    current_state = await state.get_state()
    print(current_state)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help3')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_3")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'back_to_input_3')
async def order_3_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_date=query.message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_2")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIGI2Wp6UL0G8X7XDFZV_zlJpN0h1JrAAL62jEbE81QSQpAbm4VDCgiAQADAgADeQADNAQ',
        caption="Перепиши номер кузова из свидетельства о регистрации"
    )
    await query.message.answer(
        text='<b>Укажите какой кузов у авто</b>', reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.kuzov_auto)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.kuzov_auto)
async def order_4(message: Message, state: FSMContext):
    await state.update_data(chosen_kuzov=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help4")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_3")
    )
    await message.answer(
        text="Последний, но очень важный пункт"
    )
    await message.answer(
        text='1. Бензин/дизель/гибрид \n\
2. автомат/механика \n\
3. расположение руля : правый/левый \n\n\
Напишите ответы на эти вопросы в одном сообщении в свободной форме', reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.additional_info)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    await asyncio.sleep(1800)
# Определять функцию клавы перед хендлером на который навесил
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help4')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_4")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_4')
async def order_4_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_kuzov=query.message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help4")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_3")
    )
    await query.message.answer(
        text="Последний, но очень важный пункт"
    )
    await query.message.answer(
        text='1. Бензин/дизель/гибрид \n\
2. автомат/механика \n\
3. расположение руля : правый/левый \n\n\
Напишите ответы на эти вопросы в одном сообщении в свободной форме', reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.additional_info)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    await asyncio.sleep(1800)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.additional_info)
async def order_5(message: Message, state: FSMContext):
    await state.update_data(chosen_info=message.text)
    user_data = await state.get_data()
    print(
        f"Клиент ввел имя {user_data['chosen_name']} и телефон {user_data['chosen_phone']} а так же {user_data['chosen_model']} {user_data['chosen_kuzov']} {user_data['chosen_date']} {user_data['chosen_info']} "
    )
    await message.answer(
        text='Отлично! Переходим к самому приятному блоку) Выбери то, как будут выглядеть твои будущие коврики'
    )
    await message.answer_photo(
        photo='AgACAgIAAxkDAAILzGW4jxCsUHyu1rYOJgQ02CHGRP1qAAIa1zEbQrjASfX-aIz3PtB7AQADAgADeAADNAQ'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help5")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_4")
    )
    await message.answer(
        text="Выберите тип коврика и отправь его номер в сообщении:",
        reply_markup=choice_type_of_cover()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.nashi_covriki)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help5')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_5')
async def order_5_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_info=query.message.text)
    user_data = await state.get_data()
    print(
        f"Клиент ввел имя {user_data['chosen_name']} и телефон {user_data['chosen_phone']} а так же {user_data['chosen_model']} {user_data['chosen_kuzov']} {user_data['chosen_date']} {user_data['chosen_info']} "
    )
    await query.message.answer(
        text='Отлично! Переходим к самому приятному блоку) Выбери то, как будут выглядеть твои будущие коврики'
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAILzGW4jxCsUHyu1rYOJgQ02CHGRP1qAAIa1zEbQrjASfX-aIz3PtB7AQADAgADeAADNAQ'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help5")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_4")
    )
    await query.message.answer(
        text="Выберете тип коврика и отправь его номер в сообщении:",
        reply_markup=choice_type_of_cover()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == '1_type')
async def order_5_type1(query: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_typeof='1')
    await query.message.answer('Давай уточним тип коврика.\n<b>Отправь номер в сообщении ниже:</b>\n\n\
1)Водительский коврик\n\
2)Передний пассажирский\n\
3)Задний правый\n\
4)Задний левый')
    await state.set_state(MakeOrder.nashi_covriki)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == '4_type')
async def order_5_type4(query: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_typeof='4')
    await query.message.answer('Давай уточним тип коврика.\n<b>Отправь номер в сообщении ниже:</b>\n\n\
1)Первый ряд\n\
2)Второй ряд\n\
3)Третий ряд(для автобусов и минивэнов)')
    await state.set_state(MakeOrder.nashi_covriki)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.nashi_covriki)
async def order_6_nashi(message: Message, state: FSMContext):
    await state.update_data(chosen_typeof_2=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Выбрать тип коврика",
        callback_data="choose_type_of_cover")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await message.answer_video(video='BAACAgIAAxkDAAIQxmXaI9CaijkP99RJNTzdPFiF6c-NAALmQgACoLHYSnhww4gcrLcgNAQ')
    await message.answer(
        text='Наши коврики: \n \
▫️без запаха \n \
▫️не впитывают влагу \n \
▫️ложатся без щелей и зазоров\n \
▫️легко моются и обслуживаются\n \
▫️удерживают грязь и воду, поэтому обувь остается чистой',
        reply_markup=builder.as_markup()
    )
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == '2_type')
async def order_6_nashi(query: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_typeof='2')
    await state.update_data(chosen_typeof_2='Нет')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Выбрать тип коврика",
        callback_data="choose_type_of_cover")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await query.message.answer_video(video='BAACAgIAAxkDAAIQxmXaI9CaijkP99RJNTzdPFiF6c-NAALmQgACoLHYSnhww4gcrLcgNAQ')
    await query.message.answer(
        text='Наши коврики: \n \
▫️без запаха \n \
▫️не впитывают влагу \n \
▫️ложатся без щелей и зазоров\n \
▫️легко моются и обслуживаются\n \
▫️удерживают грязь и воду, поэтому обувь остается чистой',
        reply_markup=builder.as_markup()
    )
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == '3_type')
async def order_6_nashi(query: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_typeof='3')
    await state.update_data(chosen_typeof_2='Нет')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Выбрать тип коврика",
        callback_data="choose_type_of_cover")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await query.message.answer_video(video='BAACAgIAAxkDAAIQxmXaI9CaijkP99RJNTzdPFiF6c-NAALmQgACoLHYSnhww4gcrLcgNAQ')
    await query.message.answer(
        text='Наши коврики: \n \
▫️без запаха \n \
▫️не впитывают влагу \n \
▫️ложатся без щелей и зазоров\n \
▫️легко моются и обслуживаются\n \
▫️удерживают грязь и воду, поэтому обувь остается чистой',
        reply_markup=builder.as_markup()
    )
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'back_to_order_55')
async def order_6_nashi(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_typeof=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Выбрать тип коврика",
        callback_data="choose_type_of_cover")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await query.message.answer_video(video='BAACAgIAAxkDAAIQxmXaI9CaijkP99RJNTzdPFiF6c-NAALmQgACoLHYSnhww4gcrLcgNAQ')

    await query.message.answer(
        text='Наши коврики: \n \
▫️без запаха \n \
▫️не впитывают влагу \n \
▫️ложатся без щелей и зазоров\n \
▫️легко моются и обслуживаются\n \
▫️удерживают грязь и воду, поэтому обувь остается чистой',
        reply_markup=builder.as_markup()
    )
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
# Добавить гифку

#
#
# тут надо добавить выбор ромб или сота


# @router.message(MakeOrder.type_of)
@router.callback_query(F.data == 'choose_type_of_cover')
async def order_6(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Ромб",
        callback_data="romb")
    )
    builder.add(types.InlineKeyboardButton(
        text="Сота",
        callback_data="sota")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_order_55")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIRC2Xcu0H3MAO9RP3qcvnd3Gv99MJ6AAIu2DEbk3jpSrdF6pNcVoD0AQADAgADeQADNAQ',
        caption='Выберете тип покрытия: ромб или сота \n\n\
Есть ли разница? В эксплуатации - нет. Покрытие отличаются только формой и объемом ячеек.',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.material_of)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'back_to_input_6')
async def order_6_1(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Ромб",
        callback_data="romb")
    )
    builder.add(types.InlineKeyboardButton(
        text="Сота",
        callback_data="sota")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_order_55")
    )
    await query.message.answer_photo(
        photo='AgACAgIAAxkDAAIRC2Xcu0H3MAO9RP3qcvnd3Gv99MJ6AAIu2DEbk3jpSrdF6pNcVoD0AQADAgADeQADNAQ',
        caption='Выберете тип покрытия: ромб или сота \n\n\
Есть ли разница? В эксплуатации - нет. Покрытие отличаются только формой и объемом ячеек.',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.material_of)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


# @router.callback_query(F.data == 'choose_type')
# async def ordery_7_1(query: CallbackQuery, state: FSMContext):
#     await state.set_state(MakeOrder.material_of)

@router.callback_query(F.data == 'romb')
@router.message(MakeOrder.material_of)
async def order_7(query: CallbackQuery, state: FSMContext):
    await state.update_data(romb_sota='Ромб')
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Выбери цвет коврика",
        callback_data="choose_color_1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help7")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    # await query.message.answer(text='*картинка с инфографикой с цветами"')
    await query.message.answer(
        text='Введите номер цвета коврика и цвета канта\nЦвет не влияет на стоимость ',
        reply_markup=order_7_kb()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.color_cover)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'sota')
@router.message(MakeOrder.material_of)
async def order_7(query: CallbackQuery, state: FSMContext):
    await state.update_data(romb_sota='Сота')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Выбери цвет коврика",
        callback_data="choose_color_1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help7")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    # await query.message.answer(text='*картинка с инфографикой с цветами"')
    await query.message.answer(
        text='Введите номер цвета коврика и цвета канта\nЦвет не влияет на стоимость ',
        reply_markup=order_7_kb()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.color_cover)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'choose_color_1')
async def color_cover(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help7")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    user_data = await state.get_data()
    if (user_data['romb_sota'] == 'Сота'):
        await query.message.answer_photo(photo='AgACAgIAAxkDAAIREGXcu0ZNgj2DcuTQyKVMiNC4Cb7EAAI02DEbk3jpSuDboOebi7sDAQADAgADdwADNAQ')
    else:
        await query.message.answer_photo(photo='AgACAgIAAxkDAAIRD2Xcu0azF9DPfSSZnkd0ASKrT_WnAAIz2DEbk3jpSlJ9Y4TvxXGjAQADAgADdwADNAQ')
    await query.message.answer(text='Выбери цвет коврика и напише его в поле ниже', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.cantik_color)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.cantik_color)
async def cantik_color(message: Message, state: FSMContext):
    await state.update_data(chosen_color_cover=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help7")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    await message.answer_photo(photo='AgACAgIAAxkDAAIREWXcu0bCdQQggd_zeRr6DRz1a_L-AAI12DEbk3jpShxLhFxm9ZNjAQADAgADdwADNAQ')
    await message.answer(text='Выбери цвет кантика и напиши его в поле ниже', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.color_cover)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help7')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


# @router.callback_query(F.data == 'back_to_input_8')
# async def order_7_b(query: CallbackQuery, state: FSMContext):
#     # await state.update_data(chosen_materialof=message.text)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Мне нужна помощь",
#         callback_data="help7")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Назад",
#         callback_data="back_to_input_6")
#     )
#     await query.message.answer(text='*картинка с инфографикой с цветами"')
#     await query.message.answer(
#         text='Введите номер цвета коврика и цвета канта\nЦвет не влияет на стоимость ',
#         reply_markup=builder.as_markup()
#     )
#     user_data = await state.get_data()
#     print(f'Клиент ввел данные:{user_data}')
#     await state.set_state(MakeOrder.color_cover)


# @router.message(MakeOrder.color_of)
# @router.callback_query(F.data == 'choose_color')
# async def order_7(query: CallbackQuery, state: FSMContext):
#     # await state.update_data(chosen_colorof=message.text)

#     builder = InlineKeyboardBuilder()

#     builder.add(types.InlineKeyboardButton(
#         text="Мне нужна помощь",
#         callback_data="help")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Назад",
#         callback_data="back_to_input_7")
#     )
#     await query.message.answer_dice()
#     await query.message.edit_text(text='Выбери цвет коврика и напиши его номер в поле ниже', reply_markup=builder.as_markup)
#     await state.set_state(MakeOrder.color_cover)


@router.message(MakeOrder.color_cover)
async def order_8(message: Message, state: FSMContext):
    await state.update_data(chosen_colorof=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Продолжить",
        callback_data="continue_dopnik")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help9")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    # await message.answer(text='Видео о важности допников')
    await message.answer(text='Осталось еще чуть чуть! Заполни последних важный блок! \nОт него зависит, насколько ровно лягут коврики', reply_markup=order_8_kb())
    await state.set_state(MakeOrder.color_cant)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help9')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_9")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_9')
async def order_8_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(chosen_colorof=query.message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Продолжить",
        callback_data="continue_dopnik")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help9")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    # await query.message.answer(text='Видео о важности допников')
    await query.message.answer(text='Осталось еще чуть чуть! Заполни последних важный блок! \nОт него зависит, насколько ровно лягут коврики', reply_markup=order_8_kb())
    await state.set_state(MakeOrder.color_cant)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.color_cant)
@router.callback_query(F.data == 'continue_dopnik')
async def order_9(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help10")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_9")
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDGXcu0EHgeoXKATDvG7Uv-rEt1HXAAIv2DEbk3jpSv58j4atFm3MAQADAgADeQADNAQ')
    await query.message.answer(text='<b>Укажи тип крепления для ковриков</b> \n\n \
У каждого автомобиля есть свои заводские штатные крепления:\n\
-крючки\n-штыри\n-поворотные механизмы\n\n\
Они нужны для дополнительной безопасности и фиксации, чтобы коврик случайным образом не запал под педали газа и тормоза', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.dopniki)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help10')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_10")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_10')
async def order_9_b(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help10")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_9")
    )
    await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDGXcu0EHgeoXKATDvG7Uv-rEt1HXAAIv2DEbk3jpSv58j4atFm3MAQADAgADeQADNAQ')
    await query.message.answer(text='<b>Укажи тип крепления для ковриков</b>\n\n\
У каждого автомобиля есть свои заводские штатные крепления:\n\
-крючки\n-штыри\n-поворотные механизмы\n\n\
Они нужны для дополнительной безопасности и фиксации, чтобы коврик случайным образом не запал под педали газа и тормоза', reply_markup=builder.as_markup())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.dopniki)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.dopniki)
async def order_10(message: Message, state: FSMContext):
    await state.update_data(type_of_fastening=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help10")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_10")
    )
    await message.answer_photo(photo='AgACAgIAAxkDAAIRDmXcu0VDK-5AJoG7I1zLC39bUFClAAIy2DEbk3jpSsbk8M5dTtLpAQADAgADdwADNAQ')
    await message.answer(text='<b>Выбери тип подпятника</b> \n\
Зачем он вообще нужен? Надежно защищает от вмятин и трещин, увеличивает срок службы водительского коврика', reply_markup=builder.as_markup())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.pyatka)


@router.callback_query(F.data == 'help10')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_12")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_12')
async def order_10_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(type_of_fastening=query.message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help10")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_10")
    )
    await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDmXcu0VDK-5AJoG7I1zLC39bUFClAAIy2DEbk3jpSsbk8M5dTtLpAQADAgADdwADNAQ')
    await query.message.answer(text='<b>Выбери тип подпятника</b> \n\
Зачем он вообще нужен? Надежно защищает от вмятин и трещин, увеличивает срок службы водительского коврика', reply_markup=builder.as_markup())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.pyatka)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.message(MakeOrder.pyatka)
async def order_11(message: Message, state: FSMContext):
    await state.update_data(type_of_pyatka=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Да",
        callback_data="yes_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нет",
        callback_data="no_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_12")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help11")
    )
    await message.answer_video(video='BAACAgIAAxkDAAIQzWXaJEuP6-_RhkJpAqg89KZWqSzlAALrQgACoLHYSn6jgnXCNYJXNAQ')
    await message.answer(text='Нужны ли на твои коврики шильдики? \n\
-брендируют коврики\n-улучшают визуал\n\nСмотри видео, чтобы заценить как смотрятся 🔥', reply_markup=order_11_kb())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.shield)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help11')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'back_to_input_13')
async def order_11_b(query: CallbackQuery, state: FSMContext):
    # await state.update_data(type_of_pyatka=query.message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Да",
        callback_data="yes_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нет",
        callback_data="no_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_12")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help11")
    )
    await query.message.answer_video(video='BAACAgIAAxkDAAIQzWXaJEuP6-_RhkJpAqg89KZWqSzlAALrQgACoLHYSn6jgnXCNYJXNAQ')
    await query.message.answer(text='Нужны ли на твои коврики шильдики? \n\
-брендируют коврики\n-улучшают визуал\n\nСмотри видео, чтобы заценить как смотрятся 🔥', reply_markup=order_11_kb())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.shield)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help11')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
\n\
Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.message(MakeOrder.shield)
@router.callback_query(F.data == 'yes_shield')
async def order_12_summary_y(query: CallbackQuery, state: FSMContext):
    await state.update_data(shield='Нужен')
    user_data = await state.get_data()
    # await query.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить заказ",
        callback_data="finally")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help12")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.answer_photo(photo="AgACAgIAAxkDAAIMrmXIrc4rgAqLiVMCIUg3SAW8XWIcAAK_0TEbc31IStnXm_iK3tMTAQADAgADeQADNAQ")

    await query.message.answer(text=f"\
Спасибо за заказ! Мы уже подбираем лекала под твои коврики🔥\n\
Проверь, все ли данные в заказе верны, особенно телефон\n\
Если нужно что-то поправить, напиши в поле ниже, мы разберемся :)\n\
Ваше имя: {user_data['chosen_name']}\n\
Ваш телефон: {user_data['chosen_phone']}\n\
Марка и модель: {user_data['chosen_model']}\n\
Год выпуска: {user_data['chosen_date']}\n\
Кузов авто: {user_data['chosen_kuzov']}\n\
Доп.информация: {user_data['chosen_info']}\n\
Тип коврика: {user_data['chosen_typeof']}\n\
Дополнительный тип коврика: {user_data['chosen_typeof_2']}\n\
Ячейка: {user_data['romb_sota']}\n\
Цвет канта: {user_data['chosen_colorof']}\n\
Цвет коврика: {user_data['chosen_color_cover']}\n\
Тип крепления: {user_data['type_of_fastening']}\n\
Тип подпятника: {user_data['type_of_pyatka']}\n\
Шильдик: {user_data['shield']}", reply_markup=final_kb())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.final)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help12')
async def order_12_summary_y_help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="yes_shield")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
        \n\
        Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.message(MakeOrder.shield)
@router.callback_query(F.data == 'no_shield')
async def order_12_summary_n(query: CallbackQuery, state: FSMContext):
    await state.update_data(shield='Не нужен')
    # await query.message.delete()
    user_data = await state.get_data()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить заказ",
        callback_data="finally")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help13")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.answer_photo(photo="AgACAgIAAxkDAAIMrmXIrc4rgAqLiVMCIUg3SAW8XWIcAAK_0TEbc31IStnXm_iK3tMTAQADAgADeQADNAQ")
    await query.message.answer(text=f"\
Спасибо за заказ! Мы уже подбираем лекала под твои коврики🔥\n\
Проверь, все ли данные в заказе верны, особенно телефон\n\
Если нужно что-то поправить, напиши в поле ниже, мы разберемся :)\n\
Ваше имя: {user_data['chosen_name']}\n\
Ваш телефон: {user_data['chosen_phone']}\n\
Марка и модель: {user_data['chosen_model']}\n\
Год выпуска: {user_data['chosen_date']}\n\
Кузов авто: {user_data['chosen_kuzov']}\n\
Доп.информация: {user_data['chosen_info']}\n\
Тип коврика: {user_data['chosen_typeof']}\n\
Дополнительный тип коврика: {user_data['chosen_typeof_2']}\n\
Ячейка: {user_data['romb_sota']}\n\
Цвет канта: {user_data['chosen_colorof']}\n\
Цвет коврика: {user_data['chosen_color_cover']}\n\
Тип крепления: {user_data['type_of_fastening']}\n\
Тип подпятника: {user_data['type_of_pyatka']}\n\
Шильдик: {user_data['shield']}", reply_markup=final_kb())
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.final)
    current_state = await state.get_state()
    await asyncio.sleep(time1)
# Определять функцию клавы перед хендлером на который навесил
    if (current_state == await state.get_state()):
        msg1 = await query.message.answer(text='Пссс... Пока ты думаешь, мы отшили 50 ковриков. Торопись дозаполнить заявку, чтобы получить заказ как можно скорее!\n\n\
Пока ты думал, твой салон стал грязнее\n\
потратил 3000 на химчистку\n\n\
Или просто позвони\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time2)
        await delete(msg1.chat.id, msg1.message_id)
    if (current_state == await state.get_state()):
        msg2 = await query.message.answer(text='Цвет твоих ковриков скоро может закончиться. Рекомендуем заполнить все параметры до конца.\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())
        await asyncio.sleep(time3)
        await delete(msg2.chat.id, msg2.message_id)
        print('success2')
    if (current_state == await state.get_state()):
        # await delete(msg3.chat.id, msg3.message_id)
        msg3 = await query.message.answer_photo(photo='AgACAgIAAxkDAAIRDWXcu0OCQWytsQGKv6ybxXcOAoIXAAIx2DEbk3jpSqH-kPrsJehKAQADAgADdwADNAQ', caption='Все просто: мастера заряжены, а менеджер ждет твою заявку\n\n\
Нужна помощь в подборе? Звони:\n\
+7(914)5-501-502', reply_markup=wait_kb())


@router.callback_query(F.data == 'help13')
async def order12_n_help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="no_shield")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
        \n\
        Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()
    print(f'Клиент ввел данные:{user_data}')
    await state.set_state(MakeOrder.help_state)


@router.message(MakeOrder.final)
@router.callback_query(F.data == 'finally')
async def order_13_final(query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await query.message.edit_text(text=f"\
Спасибо за заказ! Мы уже подбираем лекала под твои коврики🔥\n\
Проверь, все ли данные в заказе верны, особенно телефон\n\
Если нужно что-то поправить, напиши в поле ниже, мы разберемся :)\n\
Ваше имя: {user_data['chosen_name']}\n\
Ваш телефон: {user_data['chosen_phone']}\n\
Марка и модель: {user_data['chosen_model']}\n\
Год выпуска: {user_data['chosen_date']}\n\
Кузов авто: {user_data['chosen_kuzov']}\n\
Доп.информация: {user_data['chosen_info']}\n\
Тип коврика: {user_data['chosen_typeof']}\n\
Дополнительный тип коврика: {user_data['chosen_typeof_2']}\n\
Ячейка: {user_data['romb_sota']}\n\
Цвет канта: {user_data['chosen_colorof']}\n\
Цвет коврика: {user_data['chosen_color_cover']}\n\
Тип крепления: {user_data['type_of_fastening']}\n\
Тип подпятника: {user_data['type_of_pyatka']}\n\
Шильдик: {user_data['shield']}")
    print(f'Клиент ввел данные:{user_data}')
    await send_mail('Новый заказ!', mailto, f"\
Имя клиента: {user_data['chosen_name']}<br>\
Телефон: {user_data['chosen_phone']}<br>\
Марка и модель: {user_data['chosen_model']}<br>\
Год выпуска: {user_data['chosen_date']}<br>\
Кузов авто: {user_data['chosen_kuzov']}<br>\
Доп.информация: {user_data['chosen_info']}<br>\
Тип коврика: {user_data['chosen_typeof']}<br>\
Дополнительный тип коврика: {user_data['chosen_typeof_2']}<br>\
Ячейка: {user_data['romb_sota']}<br>\
Цвет канта: {user_data['chosen_colorof']}<br>\
Цвет коврика: {user_data['chosen_color_cover']}<br>\
Тип крепления: {user_data['type_of_fastening']}<br>\
Тип подпятника: {user_data['type_of_pyatka']}<br>\
Шильдик: {user_data['shield']}")
    await state.clear()
    await query.message.answer(text='<b>Мы свяжемся в ближайшее время для подтверждения заказа!</b>')


# загрузка фото


# Функционал
# Поправить все кнопки "Назад"
# Сделать разбор словаря с цветами канта и коврика
# Сообщения после бездействия
# Добавить await callback.answer() там где часики - мб лучше вместо этого в след хендлере ловить и редачить\удалять?


# Визуал
# Начать делать красивый текст, форматирование и отступы
# Начать добавлять картинки
# Красивая клавиатура


# Тестирование нежелательных данных, фильтры?
# Завернуть в контейнер, и запустить локально в контейнере
# Деплой контейнера на VPS
