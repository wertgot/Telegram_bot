from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import logging

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import menu_kb, silly_text_kb

from services.services import shuffle_text


silly_text_router = Router()

logger = logging.getLogger(__name__)
logger.info("router and logger started)")

bot_mode = {}


@silly_text_router.message(Command(commands="start"))
async def process_start_command(message: Message):
    bot_mode[message.from_user.id] = 0
    await message.answer(text=LEXICON_RU['/start'], reply_markup=menu_kb)


@silly_text_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=menu_kb)


# меню silly_text
@silly_text_router.message(F.text == LEXICON_RU['silly_text_btn'])
async def process_silly_text_btn(message: Message):
    await message.answer(text=LEXICON_RU['silly_text'], reply_markup=silly_text_kb)


# кнопки silly_text
@silly_text_router.message(F.text == LEXICON_RU['reverse_text_btn'])
async def process_reverse_text_btn(message: Message):
    bot_mode[message.from_user.id] = 1
    await message.answer(text=LEXICON_RU['reverse_text'])


@silly_text_router.message(F.text == LEXICON_RU['UwU_text_btn'])
async def process_UwU_text_btn(message: Message):
    bot_mode[message.from_user.id] = 2
    await message.answer(text=LEXICON_RU['UwU_text'])


@silly_text_router.message(F.text == LEXICON_RU['shuffle_text_btn'])
async def process_shuffle_text_btn(message: Message):
    bot_mode[message.from_user.id] = 3
    await message.answer(text=LEXICON_RU['shuffle_text'])


@silly_text_router.message(F.text)
async def process_text(message: Message):
    logger.debug(bot_mode)
    if bot_mode[message.from_user.id] == 0 or message.from_user.id not in bot_mode:
        await message.answer(text=LEXICON_RU['no_mode_text'], reply_markup=menu_kb)
    elif bot_mode[message.from_user.id] == 1:
        await message.answer(text=message.text[::-1])
    elif bot_mode[message.from_user.id] == 2:
        await message.answer(text=f"{message.text}\nUwU")
    elif bot_mode[message.from_user.id] == 3:
        await message.answer(text=shuffle_text(message.text))
    else:
        logger.error(
            f'''нет мода {bot_mode[message.from_user.id]} для бота\n
            {message}'''
        )