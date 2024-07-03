from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Welcome to WisdomSpherebot {message.from_user.full_name}!\n'
                         f'this bot is designed to read quotes')
    await message.delete()
