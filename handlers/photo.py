from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
# from keyboards.kb_common import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

router = Router()


@router.message(F.photo)
async def echo_gif(message: Message):
    await message.answer(message.photo.file_id)
