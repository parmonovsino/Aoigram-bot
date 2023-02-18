import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

wikipedia.set_lang('uz')

API_TOKEN = '5904607271:AAHBE_DL3Xp_a1jRMJaNpLKajcqyjyXDidI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}\nmen oddiy botman")

@dp.message_handler()
async def echo(message: types.Message):
    respons = wikipedia.summary(message.text)
    try:
        await message.answer(respons)
    except:
        await message.answer("bu mavzuga oid maqola topaolmadim")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)