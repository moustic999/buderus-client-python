import asyncio

import aiohttp

from buderus.gateway import Gateway



async def main():
    async with aiohttp.ClientSession() as session:
        gateway =  Gateway(session, '192.168.1.8','scrambled','scrambled')
        result = await gateway.get_json('/heatingCircuits/hc1/operationMode')
      
        value = result['value']
        print(result)


       


asyncio.get_event_loop().run_until_complete(main())