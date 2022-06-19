from aiogram import types

from loader import dp
import wikipedia
wikipedia.set_lang('uz')


# Echo bot
@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("🇺🇿: Bu mavzuga oid maqola topilmadi🤔\n"
                             "🇷🇺: По этой теме статей не найдено\n"
                             "🇬🇧: No articles were found on this topic")
