### Async I/O
- Async I/O is a single threaded, single process technique that uses cooperative multitasking
- Async I/O gives the feeling of concurrency despite using single process
- Coroutines are the central feature for async I/O and can be scheduled concurrently but they are not inherently concurrent
- Aync I/O takes long running tasks which blocks the program execution.It manages them in a way so other functions can run during that downtime

### Coroutines
- Coroutines is an object that can be pause its execution and resume it later. in the meantime , it can pass the control to an eventloop which can run other coroutines.
- Coroutine objects results from calling a coroutine function which is defined using async def syntax called asynchronous functions


### Async keywords
- async def - defines a coroutine function or asynchronous generator
- async for / async with -  async context manager and loop
- await - resume the execution of the surrounding coroutine and passes the control to the event loop
- - example:

```
async def g():
    result = await f()  # Pause and come back to g() when f() returns
    return result 
```
#### Rules
- we can use await, return( to return) and yield(for asynchronous generator) inside a coroutine (async def) function
- yield from is not support and it throws syntax error
- Note that all the above are optional, we can run coroutine directly in the event loop without return anything
- await cannot be used outside coroutine function

# Run Async func without using asyncio.run()
- we can run async function without using asyncio.run() by using event loop directly using asyncio REPL
```$ python -m asyncio
>>> import asyncio
>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')
...
>>> await main()
hello
world
```     


