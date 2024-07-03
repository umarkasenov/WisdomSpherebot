from aiogram import Bot, Dispatcher
from os import getenv

API_TOKEN = getenv('API_TOKEN')
bot = Bot(API_TOKEN)
dp = Dispatcher()

if API_TOKEN is None:
    raise ValueError("No API token provided. Please set the API_TOKEN environment variable.")
