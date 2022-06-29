from create_bot import dp
from aiogram import executor
import logging
from handlers import client

logging.basicConfig(level=logging.INFO)


client.dp_registerhandlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
