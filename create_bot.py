from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API ='BOT TOKEN'

storage = MemoryStorage()

bot = Bot(token=API)
dp = Dispatcher(bot,storage=storage)
