import asyncio


async def foo():
    await asyncio.sleep(0)
    print("Hello")


async def bar():
    print("Bye")


async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)


# asyncio.run(foo())
# asyncio.run(bar())

# tasks = [foo(), bar()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()


asyncio.run(main())
