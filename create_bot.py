from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API ='5432923971:AAF6_kU0wsBmlvS4eDG5UHwnOPTkMUv5iwc'

storage = MemoryStorage()

bot = Bot(token=API)
dp = Dispatcher(bot,storage=storage)