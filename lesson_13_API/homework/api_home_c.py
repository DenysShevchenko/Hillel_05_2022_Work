import asyncio
import random
from time import perf_counter

import httpx

# import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 1


def get_random_id():
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_pokemon_async(id_: str):
    url = BASE_URL + id_
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()["name"]
    # async with aiohttp.ClientSession() as client:
    #     async with client.get(url) as resp:
    #         r = 2
    #         # resp_j = await resp.json()
    #         # r = resp_j.get('name')
    #     return client


async def get_random_pokemon_async():
    random_id = get_random_id()
    return await get_pokemon_async(random_id)


async def async_main():
    tasks = [get_random_pokemon_async() for _ in range(SIZE)]
    random_pokemons = await asyncio.gather(*tasks)
    print(f"Pokemons: {random_pokemons}")


def main():
    print("=" * 30)

    # NOTE: Async run
    start_time = perf_counter()
    asyncio.run(async_main())

    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time}")


if __name__ == "__main__":
    main()
