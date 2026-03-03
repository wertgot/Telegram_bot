from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import(
    Message,
    CallbackQuery,
    ReactionTypeEmoji,
)

import logging

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import gay_check_kb


gay_check_router = Router()

logger = logging.getLogger(__name__)

@gay_check_router.message(F.text == LEXICON_RU["gay_check_btn"])
async def process_start_command(message: Message):
    await message.answer(
        text="Ты крутой?", reply_markup=gay_check_kb
    )


@gay_check_router.callback_query(F.data == "yes_gay_btn_click")
async def process_yes_gay_btn_click(callback: CallbackQuery):
    if callback.message.text != "Ты гей?":
        await callback.message.edit_text(
            text="Ты гей?",
            reply_markup=callback.message.reply_markup,
        )
        await callback.message.react([ReactionTypeEmoji(emoji="👍")])
    await callback.answer()


@gay_check_router.callback_query(F.data == "no_gay_btn_click")
async def process_no_gay_btn_click(callback: CallbackQuery):
    if callback.message.text != "Ты гей?":
        await callback.answer(text='печально(')
    else:
        await callback.answer(text='не отнекивайся', show_alert=True)
