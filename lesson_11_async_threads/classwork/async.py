import asyncio

from services import get_random_countdown, get_random_delay


async def launch_rocket(name: int, countdown: int, delay: float) -> None:
    print(f"Launching rocket #{name}")
    for i in reversed(range(1, countdown)):
        print(f"{i}...")
        await asyncio.sleep(1)

    print(f"Delay for {delay}")
    await asyncio.sleep(delay)

    print("Rocket in the space")


def main():
    N = 10_000
    tasks = [
        launch_rocket(
            i,
            get_random_countdown(),
            get_random_delay(),
        )
        for i in range(1, N + 1)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


if __name__ == "__main__":
    main()
