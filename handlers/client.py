from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from handlers.States import GetUsername
from keyboards import find_button_kb,get_res_kb
import aiohttp
import asyncio
from datetime import datetime
import sys
import json
import time
import blackbird


file = open('handlers/data.json')
searchData = json.load(file)
currentOs = sys.platform



async def send_welcome(message: types.Message):
    await message.reply('''Powered by mays126 and p1ngul1n0''',reply_markup=find_button_kb)

async def find_start(message: types.Message):
    await message.reply('Enter nickname')
    await GetUsername.username.set()

async def find_get_username(message: types.Message, state: FSMContext):
    await message.reply('Search for info...')
    async with state.proxy() as data:
        data['username'] = message.text
        username = data['username']
        proxy = "http://127.0.0.1:8080"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
        }

        start_time = time.time()
        timeout = aiohttp.ClientTimeout(total=10)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            tasks = []
            for u in searchData["sites"]:
                task = asyncio.ensure_future(blackbird.makeRequest(session, u, username))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            executionTime = round(time.time() - start_time, 1)
            userJson = {"search-params": {"username": username, "sites-number": len(searchData['sites']), "date": now,
                                          "execution-time": executionTime}, "sites": []}
            for x in results:
                userJson["sites"].append(x)
                answer = ''

                if x['error-message'] == 'TimeoutError()':
                    continue
                else:
                    if x['metadata']:
                        for j in x['metadata']:
                            site_metadata = ''
                            site_metadata += f'''{j["key"]}:{j["value"]}\n'''
                        answer = f'''Site: {x["app"]}
Status: {x["status"]}
URL: {x["url"]}
Metadata: 
{site_metadata}'''
                        await message.answer(answer)
                    else:
                        answer = f'''Site: {x["app"]}
Status: {x["status"]}
URL: {x["url"]}
'''
                        await message.answer(answer)





def dp_registerhandlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(find_start,Text(equals='Start Finding',ignore_case=True),state=None)
    dp.register_message_handler(find_get_username,state=GetUsername.username)



