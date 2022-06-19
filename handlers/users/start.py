from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 {message.from_user.full_name}\n"
                         f"🇺🇿: Wikipedia botiga xush kelibsiz !\n"
                         f"🇷🇺: Добро пожаловать в Википедию\n"
                         f"🇬🇧: Welcome to Wikipedia", reply_markup=menu)
