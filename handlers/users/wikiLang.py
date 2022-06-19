from aiogram import types
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
import wikipedia

from keyboards.inline.callback_data import setLang_callback
from loader import dp
from states.SetLangSatates import SetLangstates

# Wiki Set Lang UZ
@dp.callback_query_handler(setLang_callback.filter(item_name="languz"), state=None)
async def set_uz(call: CallbackQuery):
    await call.answer("Til o'zgartirildi ! 🇺🇿", cache_time=60, show_alert=True)
    await SetLangstates.Languz.set()
    await call.message.delete()

@dp.message_handler(state=SetLangstates.Languz)
async def sendWiki(message: types.Message, state: FSMContext):
    wikipedia.set_lang('uz')
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi🤔")
    await state.reset_state(with_data=False)

# Wiki Set Lang RU
@dp.callback_query_handler(setLang_callback.filter(item_name="langru"), state=None)
async def set_ru(call: CallbackQuery):
    await call.answer("Язык изменен ! 🇷🇺", cache_time=60, show_alert=True)
    await SetLangstates.Langru.set()
    await call.message.delete()

@dp.message_handler(state=SetLangstates.Langru)
async def sendWiki(message: types.Message, state: FSMContext):
    wikipedia.set_lang('ru')
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("По этой теме статей не найдено🤔")
    await state.reset_state(with_data=False)

# Wiki Set Lang EN
@dp.callback_query_handler(setLang_callback.filter(item_name="langen"), state=None)
async def set_en(call: CallbackQuery):
    await call.answer("Language changed ! 🇬🇧", cache_time=60, show_alert=True)
    await SetLangstates.Langen.set()
    await call.message.delete()

@dp.message_handler(state=SetLangstates.Langen)
async def sendWiki(message: types.Message, state: FSMContext):
    wikipedia.set_lang('en')
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("No articles were found on this topic🤔")
    await state.reset_state(with_data=False)