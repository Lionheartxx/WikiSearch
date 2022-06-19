from aiogram.types import Message
from keyboards.inline.setLang import LangMenu

from loader import dp

@dp.message_handler(text_contains="Settings")
async def select_category(message: Message):
    await message.answer(f"🇺🇿 - Tilni tanlang 👇\n"
                         f"🇷🇺 - Выберите язык\n"
                         f"🇬🇧 - Select a language", reply_markup=LangMenu)