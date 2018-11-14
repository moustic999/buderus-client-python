import asyncio
import sys

import aiohttp

from buderus.gateway import Gateway

# access_key = 'pAtgNvhjdJ2LFJS2'
# password = 'isnbtm0'

async def main():
    async with aiohttp.ClientSession() as session:
        gateway =  Gateway(session, '192.168.1.8','pAtgNvhjdJ2LFJS2','isnbtm0')
        result = await gateway.get_json('/heatingCircuits/hc1/operationMode')
      
        value = result['value']
        print(result)


       


asyncio.get_event_loop().run_until_complete(main())