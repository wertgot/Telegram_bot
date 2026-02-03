from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_help_command(message: Message):
    await message.answer(
        'Hello, bitch!' if message.text == '/start'
        else 'i cant help u'
    )


async def send_photo_echo(message: Message):
    await message.answer_photo(message.photo[0].file_id, caption='подпись')


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(text='Не засирай чат хуйней')


dp.message.register(
    process_start_help_command,
    Command(commands=['start', 'help'])
)
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)