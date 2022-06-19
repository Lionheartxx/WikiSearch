from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import setLang_callback

languages = {
    "UZ 🇺🇿": "languz",
    "RU 🇷🇺": "langru",
    "EN 🇬🇧": "langen",
}
LangMenu = InlineKeyboardMarkup(row_width=1)
for key, value in languages.items():
    LangMenu.insert(InlineKeyboardButton(text=key, callback_data=setLang_callback.new(item_name=value)))