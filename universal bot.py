import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

API_TOKEN = '5755780696:AAHgR_s10fUuvjYgUwISYwgXza2Qm1ABZuU'
channel_id = '-1001781579548'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

btn = KeyboardButton("πΊπΏ Uzbek - English πΊπΈ")
btn1 = KeyboardButton("πΊπΈ English - Uzbek πΊπΏ")
btn2 = KeyboardButton("πΊπΏ Uzbek - Russian π·πΊ")
btn3 = KeyboardButton("π·πΊ Russian - Uzbek πΊπΏ")
btn4 = KeyboardButton("πΊπΏ Uzbek - China π¨π³")
btn5 = KeyboardButton("π¨π³ China - Uzbek πΊπΏ")
btn6 = KeyboardButton("πΊπΏ Uzbek - German π©πͺ")
btn7 = KeyboardButton("π©πͺ German - Uzbek πΊπΏ")
btn8 = KeyboardButton("πΊπΏ Uzbek - Turkish πΉπ·")
btn9 = KeyboardButton("πΉπ· Turkish - Uzbek πΊπΏ")
btn0 = KeyboardButton("πΊπΏ Uzbek - Korean π°π·")
btn10 = KeyboardButton("π°π· Korean - Uzbek πΊπΏ")
btn11 = KeyboardButton("πΊπΏ Uzbek - Arabic")
btn12 = KeyboardButton("Arabic - Uzbek πΊπΏ")
btn13 = KeyboardButton("πΊπΏ Uzbek - Japanese π―π΅")
btn14 = KeyboardButton("π―π΅ Japanese - Uzbek πΊπΏ")
RKM = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btn10, btn11, btn12, btn13, btn14
)

ikb = InlineKeyboardButton("βAZO BO'LISH", url="t.me/it_blogi")
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
        if lang == "πΊπΏ Uzbek - English πΊπΈ":
            tarjima = tarjimon.translate(text, dest='en')
            await message.answer(tarjima.text)
        elif lang == "πΊπΈ English - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - Russian π·πΊ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "π·πΊ Russian - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - China π¨π³":
            tarjima = tarjimon.translate(text, dest='zh-cn')
            await message.answer(tarjima.text)
        elif lang == "π¨π³ China - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - German π©πͺ":
            tarjima = tarjimon.translate(text, dest='de')
            await message.answer(tarjima.text)
        elif lang == "π©πͺ German - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - Turkish πΉπ·":
            tarjima = tarjimon.translate(text, dest='tr')
            await message.answer(tarjima.text)
        elif lang == "πΉπ· Turkish - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - Korean π°π·":
            tarjima = tarjimon.translate(text, dest='ko')
            await message.answer(tarjima.text)
        elif lang == "π°π· Korean - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - Arabic":
            tarjima = tarjimon.translate(text, dest='ar')
            await message.answer(tarjima.text)
        elif lang == "Arabic - Uzbek πΊπΏ":
            tarjima = tarjimon.translate(text, dest='uz')
            await message.answer(tarjima.text)
        elif lang == "πΊπΏ Uzbek - Japanese π―π΅":
            tarjima = tarjimon.translate(text, dest='ja')
            await message.answer(tarjima.text)
        elif lang == "π―π΅ Japanese - Uzbek πΊπΏ":
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