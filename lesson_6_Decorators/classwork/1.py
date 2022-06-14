from datetime import datetime
from os import listdir

PREFIX = "./lesson_6_decorators/"
LOG_FILE = PREFIX + "actions.log"


def get_log_message(username: str, message: str) -> str:
    return f"{datetime.now()} {username}: {message}"


def log_action(text: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"{text}\n")


def read_usb(username: str):
    log_action(get_log_message(username, "Opened USB"))
    files = listdir(PREFIX + "f-disc/")
    filtered = [file for file in files if not file.startswith(".")]
    return filtered


def read_cd(username: str):
    log_action(get_log_message(username, "Opened Cd"))
    return listdir(PREFIX + "c-disc/")


def main():
    username = input("Enter your name: ")

    if not username:
        raise ValueError("No username specified...")

    while user_inp := input("Enter the option [usb / cd]: "):
        if user_inp == "cd":
            files = read_cd(username)
        elif user_inp == "usb":
            files = read_usb(username)
        else:
            print("Wrong input. Please use options from brackets!\n")
            log_action(f"{datetime.now()} {username}: Bad input - {user_inp}")
            continue

        for file in files:
            print("File:", file, sep=" ")
            print("=" * 10)

    print("Goodbye")


if __name__ == "__main__":
    main()
