
import base64
import json
import binascii

import asyncio
import aiohttp

from buderus.encryption import Encryption
from io import StringIO
      

async def fetch(session):
    magic = bytearray.fromhex("867845e97c4e29dce522b9a7d3a3e07b152bffadddbed7f5ffd842e9895ad1e4")

    access_key = 'pAtgNvhjdJ2LFJS2'
    password = 'isnbtm0'

    encryption = Encryption(magic, access_key, password)

    headers = {'User-agent': 'TeleHeater/2.2.3' ,'Accept': 'application/json'}

    print('Query http://httpbin.org/get')
    async with session.get(
            'http://192.168.1.8/dhwCircuits',headers=headers) as resp:
        print(resp.status)
        if resp.status != 200:
            return
        data = await resp.text()
        print(data)
        result = encryption.decrypt(data)
        j = json.load(StringIO(result))
        print(j)


async def go(loop):
    headers = {'User-agent': 'TeleHeater/2.2.3' ,'Accept': 'application/json'}
    
    async with aiohttp.ClientSession(loop=loop) as session:
        await fetch(session)


loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
loop.close()