from time import sleep

from services import get_random_countdown, get_random_delay


def launch_rocket(name: int, countdown: int, delay: float) -> None:
    print(f"Launching rocket #{name}")
    for i in reversed(range(1, countdown)):
        print(f"{i}...")
        sleep(1)

    print(f"Delay for {delay}")
    sleep(delay)

    print("Rocket in the space")


def main():
    N = 10_000
    for i in range(1, N + 1):
        countdown = get_random_countdown()
        delay = get_random_delay()
        launch_rocket(i, countdown, delay)


if __name__ == "__main__":
    main()
