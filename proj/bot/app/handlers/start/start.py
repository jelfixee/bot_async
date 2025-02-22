from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.app.keyboards.reply.reply import main

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    keyboard = main
    await message.answer("Выберите каталог", reply_markup=keyboard)
