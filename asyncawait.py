import time
import asyncio
async def f():
    await asyncio.sleep(5)
    return "hello"
async def g():
    a  = await f()
    return a+ " Dharun"
res = asyncio.run(g())
print(res)


asyncio.gather()