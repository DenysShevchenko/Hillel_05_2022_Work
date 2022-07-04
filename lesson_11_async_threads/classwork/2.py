# from typing import Callable


# def run_function(function: Callable, *args, **kwargs):
#     function(*args, **kwargs)


# def write_name(name: str):
#     print(f"Hello {name}")


# # write_name("Dima")

# run_function(write_name, "Dima")

import asyncio

from services import get_random_countdown, get_random_delay


async def countdown():
    value: int = get_random_countdown()
    await asyncio.sleep(value)
    print("Countdown")


async def delay():
    value: float = get_random_delay()
    await asyncio.sleep(value)
    print("Delay")


tasks = [countdown(), delay()]
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()

# asyncio.run(foo())
# asyncio.run(bar())
