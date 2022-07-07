import asyncio
import random
from time import perf_counter

import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 10


def get_random_id():
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_random_pokemon():
    url = BASE_URL + get_random_id()
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            resp_j = await resp.json()
            r = resp_j.get("name")
            # client.close()
            return r
    # client.close()
    # return r
    # async with client.get(url) as resp:
    # #     print('2')
    # # # resp = client.get(url)
    # # return '1'
    #     resp_j = await resp.json()
    #     nam = resp_j.get('name')
    #     # print(nam)
    #     return nam


async def async_main():
    tasks = [get_random_pokemon() for _ in range(SIZE)]
    random_pokemons = await asyncio.gather(*tasks)
    print(f"Pokemons: {random_pokemons}")


def main():
    # NOTE: Async run
    start_time = perf_counter()

    # tasks = [get_random_pokemon() for _ in range(SIZE)]
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()

    asyncio.run(async_main())
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time}")


if __name__ == "__main__":
    main()
