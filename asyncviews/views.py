import asyncio
from django.http import HttpResponse
from time import sleep

import httpx


async def timer():
    for num in range(1,50):
        print(num)
        await asyncio.sleep(1)
        
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(timer())
    return HttpResponse("Você não vê o tempo passando...")    