import asyncio
from aiogram import Router
from config import dp, bot
from handlers import (
    start_router,
    echo_router,
    help_router,
)


router = Router()
dp.include_router(start_router)
dp.include_router(echo_router)
dp.include_router(help_router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
