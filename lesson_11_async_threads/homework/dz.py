from threading import Thread
import random
import asyncio


def options_list(vyd, list_el):
    if vyd == 1:
        print("Поток 1 (заповнюємо список)")
        for i in range(1, 10001):
            list_el.append(random.randint(1, 100))
    elif vyd == 2:
        print("Поток 2 (сумма єлементів): " + str(sum(list_el)))
    elif vyd == 3:
        sred_zn = 0
        kol_el = len(list_el)
        if kol_el != 0:
            sred_zn = sum(list_el) / kol_el
        print("Поток 3 (середнє значення): " + str(sred_zn))


def main():
    list_el = []
    threads = [
        Thread(target=options_list, kwargs={"vyd": i, "list_el": list_el})
        for i in range(1, 4)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Частина 2 домашнього завдання
    numbers = [40000, 400, 100000, 700]
    tasks = [get_primes_amount(num) for num in numbers]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


async def get_primes_amount(num):
    print("Починаємо опрацювання число " + str(num))
    results = 0
    for i in range(num + 1):
        await asyncio.sleep(0)
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        results += 1
    print("Закінчили опрацювання числа " + str(num) + " рез: " + str(results))
    return results


if __name__ == "__main__":
    main()
