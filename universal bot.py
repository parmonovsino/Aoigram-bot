import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

API_TOKEN = '5663157501:AAELIUYnoDMrUdSUdsJomnFuHI_xN883Dww'
channel_id = '-1001781579548'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

btn = KeyboardButton("🇺🇿 Uzbek - English 🇺🇸")
btn1 = KeyboardButton("🇺🇸 English - Uzbek 🇺🇿")
btn2 = KeyboardButton("🇺🇿 Uzbek - Russian 🇷🇺")
btn3 = KeyboardButton("🇷🇺 Russian - Uzbek 🇺🇿")
btn4 = KeyboardButton("🇺🇿 Uzbek - China 🇨🇳")
btn5 = KeyboardButton("🇨🇳 China - Uzbek 🇺🇿")
btn6 = KeyboardButton("🇺🇿 Uzbek - German 🇩🇪")
btn7 = KeyboardButton("🇩🇪 German - Uzbek 🇺🇿")
btn8 = KeyboardButton("🇺🇿 Uzbek - Turkish 🇹🇷")
btn9 = KeyboardButton("🇹🇷 Turkish - Uzbek 🇺🇿")
btn0 = KeyboardButton("🇺🇿 Uzbek - Korean 🇰🇷")
btn10 = KeyboardButton("🇰🇷 Korean - Uzbek 🇺🇿")
btn11 = KeyboardButton("🇺🇿 Uzbek - Arabic")
btn12 = KeyboardButton("Arabic - Uzbek 🇺🇿")
btn13 = KeyboardButton("🇺🇿 Uzbek - Japanese 🇯🇵")
btn14 = KeyboardButton("🇯🇵 Japanese - Uzbek 🇺🇿")
RKM = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btn10, btn11, btn12, btn13, btn14
)

ikb = InlineKeyboardButton("➕AZO BO'LISH", url="t.me/it_blogi")
IKM = InlineKeyboardMarkup().add(ikb)

button = KeyboardButton("tilni o'zgartirish")
Button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(button)

class Translate(StatesGroup):
    lang = State()
    trans = State()

@dp.message_handler(CommandStart(), state='*')
async def send_welcome(message: types.Message):
    check = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if check['status'] == 'left':
        await message.reply(f"salom {message.from_user.full_name}\nmen ishlashim uchun kanalga azo bo'ling", reply_markup=IKM)
    else:
        await message.reply(f"salom {message.from_user.full_name}\nmen tarjimon botman\n\ntugmalardan birini tanlang", reply_markup=RKM)
        await Translate.lang.set()

@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data({'lang': lang})
    await message.answer("tarjima qilish uchun so'z kiriting")
    await Translate.next()

@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    check = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if check['status'] == 'left':
        await message.reply(f"salom {message.from_user.full_name}\nmen ishlashim uchun kanalga azo bo'ling", reply_markup=IKM)
    else:
        text = message.text
        data = await state.get_data()
        lang = data.get("lang")
        tarjimon = Translator()
        if lang == "🇺🇿 Uzbek - English 🇺🇸":
            tarjima = tarjimon.translate(text, dest='en')
            await message.answer(tarjima.text)
        elif lang == "🇺🇸 English - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - Russian 🇷🇺":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇷🇺 Russian - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - China 🇨🇳":
            tarjima = tarjimon.translate(text, dest='zh-cn')
            await message.answer(tarjima.text)
        elif lang == "🇨🇳 China - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - German 🇩🇪":
            tarjima = tarjimon.translate(text, dest='de')
            await message.answer(tarjima.text)
        elif lang == "🇩🇪 German - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - Turkish 🇹🇷":
            tarjima = tarjimon.translate(text, dest='tr')
            await message.answer(tarjima.text)
        elif lang == "🇹🇷 Turkish - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - Korean 🇰🇷":
            tarjima = tarjimon.translate(text, dest='ko')
            await message.answer(tarjima.text)
        elif lang == "🇰🇷 Korean - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - Arabic":
            tarjima = tarjimon.translate(text, dest='ar')
            await message.answer(tarjima.text)
        elif lang == "Arabic - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "🇺🇿 Uzbek - Japanese 🇯🇵":
            tarjima = tarjimon.translate(text, dest='ja')
            await message.answer(tarjima.text)
        elif lang == "🇯🇵 Japanese - Uzbek 🇺🇿":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        await Translate.trans.set()

@dp.message_handler()
async def echo(message: types.Message):
    check = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if check['status'] == 'left':
        await message.reply(f"salom {message.from_user.full_name}\nmen ishlashim uchun kanalga azo bo'ling", reply_markup=IKM)
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
