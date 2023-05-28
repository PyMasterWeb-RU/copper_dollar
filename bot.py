import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import markups as nav
from main import medium, dollars, copper_rub, price_change

load_dotenv()

TOKEN: str = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет {0.first_name}!".format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "💵Курс доллара":
        dollar = dollars()
        await bot.send_message(message.from_user.id, f"Курс доллара: $1 = {dollar} рублей")
    elif message.text == "🗿Курс меди в $":
        copper = medium()
        await bot.send_message(message.from_user.id, f"Курс меди в $: 1 тонна меди = {copper} $")
    elif message.text == "🔶 Курс меди в руб.":
        copper_ru = copper_rub()
        await bot.send_message(message.from_user.id, f"Курс меди в рулбях: 1 тонна меди = {copper_ru} рублей")
    elif message.text == "📈Цена сдачи в рублях":
        price = price_change()
        await bot.send_message(message.from_user.id, f"Цена сдачи в рублях: {price} рублей")
    else:
        await bot.send_message(message.from_user.id, "Неизвестная команда")
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
