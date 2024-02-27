from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def wait_kb():
    buttons = [
        [
            InlineKeyboardButton(
                text="Продолжить подбор", callback_data="pricol"),
            InlineKeyboardButton(
                text="Начать сначала", callback_data="Back_to_start")
        ],
        [InlineKeyboardButton(text="Напишите мне", callback_data="textme"),
         InlineKeyboardButton(text="Перезвоните мне", callback_data="callme")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def wait_kb_2():
    buttons = [
        [
            InlineKeyboardButton(
                text="Продолжить подбор", callback_data="Super"),
            InlineKeyboardButton(
                text="Начать сначала", callback_data="Back_to_start")
        ],
        [InlineKeyboardButton(text="Напишите мне", callback_data="textme"),
         InlineKeyboardButton(text="Перезвоните мне", callback_data="callme")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def wait_kb_3():
    buttons = [
        [
            InlineKeyboardButton(
                text="Продолжить подбор", callback_data="Super"),
            InlineKeyboardButton(
                text="Начать сначала", callback_data="Back_to_start")
        ],
        [InlineKeyboardButton(text="Напишите мне", callback_data="textme"),
         InlineKeyboardButton(text="Перезвоните мне", callback_data="callme")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def wait_kb_4():
    buttons = [
        [
            InlineKeyboardButton(
                text="Продолжить подбор", callback_data="Super"),
            InlineKeyboardButton(
                text="Начать сначала", callback_data="Back_to_start")
        ],
        [InlineKeyboardButton(text="Напишите мне", callback_data="textme"),
         InlineKeyboardButton(text="Перезвоните мне", callback_data="callme")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def wait_kb_5():
    buttons = [
        [
            InlineKeyboardButton(
                text="Продолжить подбор", callback_data="Super"),
            InlineKeyboardButton(
                text="Начать сначала", callback_data="Back_to_start")
        ],
        [InlineKeyboardButton(text="Напишите мне", callback_data="textme"),
         InlineKeyboardButton(text="Перезвоните мне", callback_data="callme")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_type_of_cover():
    buttons = [
        [
            InlineKeyboardButton(
                text="1", callback_data="1_type"),
            InlineKeyboardButton(
                text="2", callback_data="2_type"),
            InlineKeyboardButton(
                text="3", callback_data="3_type"),
            InlineKeyboardButton(
                text="4", callback_data="4_type")
        ],
        [InlineKeyboardButton(text="Мне нужна помощь", callback_data="help5"),
         InlineKeyboardButton(text="Назад", callback_data="back_to_input_4")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def start_kb():
    buttons = [
        [InlineKeyboardButton(text='Супер! Приступим к подбору',
                              callback_data="Super")],
        [InlineKeyboardButton(text='Мне нужна помощь',
                              callback_data="help")],
        [InlineKeyboardButton(text='Назад', callback_data="Back_to_start")],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def order_1_kb():
    buttons = [
        [InlineKeyboardButton(text='Указать параметры моего авто',
                              callback_data="auto")],
        [InlineKeyboardButton(text='Мне нужна помощь',
                              callback_data="help1")],
        [InlineKeyboardButton(text='Назад', callback_data="Back")],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def order_7_kb():
    buttons = [
        [InlineKeyboardButton(text='Выбери цвет коврика',
                              callback_data="choose_color_1")],
        [InlineKeyboardButton(text='Мне нужна помощь',
                              callback_data="help7")],
        [InlineKeyboardButton(text='Назад', callback_data="back_to_input_6")],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def order_8_kb():
    buttons = [
        [InlineKeyboardButton(text='Продолжить',
                              callback_data="continue_dopnik")],
        [InlineKeyboardButton(text='Мне нужна помощь',
                              callback_data="help9")],
        [InlineKeyboardButton(text='Назад', callback_data="back_to_input_6")],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def order_11_kb():
    buttons = [
        [InlineKeyboardButton(text='Да', callback_data="yes_shield"),
         InlineKeyboardButton(text='Нет', callback_data="no_shield")],
        [InlineKeyboardButton(text="Мне нужна помощь",
                              callback_data="help11")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_input_12")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def final_kb():
    buttons = [
        [InlineKeyboardButton(text='Оформить заказ',
                              callback_data="finally")],
        [InlineKeyboardButton(text='Мне нужна помощь',
                              callback_data="help12")],
        [InlineKeyboardButton(text='Назад', callback_data="back_to_input_13")],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
