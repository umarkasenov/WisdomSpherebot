from aiogram import Router, types
from aiogram.filters import Command

help_router = Router()


@help_router.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Write your problem @casen0v_1 to administrator')
    await message.delete()
