from aiogram.types import(
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


silly_text_btn = KeyboardButton(text=LEXICON_RU["silly_text_btn"])
gay_check_btn = KeyboardButton(text=LEXICON_RU["gay_check_btn"])

menu_kb_builer = ReplyKeyboardBuilder()

menu_kb_builer.row(silly_text_btn, gay_check_btn, width=1)

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


yes_gay_btn = InlineKeyboardButton(
    text="ДА", callback_data="yes_gay_btn_click"
)
no_gay_btn = InlineKeyboardButton(
    text="НЕТ", callback_data="no_gay_btn_click"
)

gay_check_kb = InlineKeyboardMarkup(inline_keyboard=[[yes_gay_btn, no_gay_btn]])
