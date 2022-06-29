from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

find_button = KeyboardButton('Start Finding')
find_button_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
find_button_kb.add(find_button)

get_res = KeyboardButton('Get results')
get_res_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
get_res_kb.add(get_res)