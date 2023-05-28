from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('ГлавноеМеню')

# Главное меню
btnDollars = KeyboardButton('💵Курс доллара')
btnMedium = KeyboardButton('🗿Курс меди в $')
btnMediumRub = KeyboardButton('🔶 Курс меди в руб.')
btnAllInfo = KeyboardButton('📈Цена сдачи в рублях')
# btnGrafic = KeyboardButton('Посмотреть график')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDollars, btnMedium, btnMediumRub, btnAllInfo)
