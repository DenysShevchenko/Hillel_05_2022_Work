from datetime import datetime
from os import listdir

PREFIX = "./lesson_6_Decorators/"
LOG_FILE = PREFIX + "actions.log"


def log(message: str):
    def wrapper(func):
        def inner(username):
            text = f"{datetime.now()} {username}: {message}"
            with open(LOG_FILE, "a") as f:
                f.write(f"{text}\n")

            return func(username)

        return inner

    return wrapper


@log(message="Reading USB")
def read_usb(username: str):
    files = listdir(PREFIX + "f-disc/")
    filtered = [file for file in files if not file.startswith(".")]
    return filtered


@log(message="Reading CD")
def read_cd(username: str):
    return listdir(PREFIX + "c-disc/")


def main():
    username = input("Enter your name: ")

    if not username:
        raise ValueError("No username specified...")

    while user_input := input("Enter the option [usb / cd]: "):
        if user_input == "cd":
            files = read_cd(username)
        elif user_input == "usb":
            files = read_usb(username)
        else:
            print("Wrong input. Please use options from brackets!\n")
            continue

        for file in files:
            print("File:", file, sep=" ")
            print("=" * 10)

    print("Goodbye")


if __name__ == "__main__":
    main()
