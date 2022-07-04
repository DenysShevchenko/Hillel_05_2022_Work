from threading import Thread
from time import sleep

from services import get_c, get_d


def laun_r(n: int, c_down: int, dela: float) -> None:
    print(f"Launching rocket #{n}")
    for i in reversed(range(1, c_down)):
        print(f"{i}...")
        sleep(1)

    print(f"Delay for {dela}")
    sleep(dela)

    print("Rocket in the space")


def main():
    N = 1000

    threads = [
        Thread(target=laun_r, kwargs={"n": i, "c_down": get_c(), "dela": get_d()})
        for i in range(1, N + 1)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
