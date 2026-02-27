from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


silly_text_btn = KeyboardButton(text=LEXICON_RU["silly_text_btn"])

menu_kb_builer = ReplyKeyboardBuilder()

menu_kb_builer.row(silly_text_btn, width=1)

menu_kb: ReplyKeyboardMarkup = menu_kb_builer.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)


reverse_text_btn = KeyboardButton(text=LEXICON_RU["reverse_text_btn"])
shuffle_text_btn = KeyboardButton(text=LEXICON_RU["shuffle_text_btn"])
UwU_text_btn = KeyboardButton(text=LEXICON_RU["UwU_text_btn"])

silly_text_kb_builer = ReplyKeyboardBuilder()

silly_text_kb_builer.row(reverse_text_btn, shuffle_text_btn, UwU_text_btn, width=1)

silly_text_kb: ReplyKeyboardMarkup = silly_text_kb_builer.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)