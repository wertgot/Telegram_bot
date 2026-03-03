from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
    ReactionTypeEmoji,
)

# Создаем объекты бота и диспетчера
bot = Bot('***REMOVED***')
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
button_1 = InlineKeyboardButton(
    text="ДА", callback_data="button_1_click"
)
button_2 = InlineKeyboardButton(
    text="НЕТ", callback_data="button_2_click"
)
# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Ты крутой?", reply_markup=keyboard
    )


# ...

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data `button_1_click`
@dp.callback_query(F.data == "button_1_click")
async def process_button_1_click(callback: CallbackQuery):
    if callback.message.text != "Ты гей?":
        await callback.message.edit_text(
            text="Ты гей?",
            reply_markup=callback.message.reply_markup,
        )
        await callback.message.react([ReactionTypeEmoji(emoji="👍")])
    await callback.answer()

@dp.callback_query(F.data == "button_2_click")
async def process_button_2_click(callback: CallbackQuery):
    await callback.answer(text='печально(')

if __name__ == "__main__":
    dp.run_polling(bot)