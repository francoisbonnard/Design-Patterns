import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)  # pause the execution of the coroutine for 1 second
    print("Coroutine finished")

async def main():
    await my_coroutine()
    print("main finish")

# Python 3.7+
asyncio.run(main())
