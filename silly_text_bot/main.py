import logging
import asyncio

from config.config import Config, load_config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.silly_text import silly_text_router


logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()

    logging.basicConfig(
        level=logging.getLevelName(config.log.level),
        format=config.log.format,
    )

    logger.info('log just started, yo :3')

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ),
    )
    dp = Dispatcher()

    dp.include_router(silly_text_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
