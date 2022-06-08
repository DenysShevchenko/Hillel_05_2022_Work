from random import choice
from string import ascii_letters

print(ascii_letters, "/n")


def gen_pass(n: int):
    text = ""

    for i in range(n):
        text += choice(ascii_letters)

    return text


my_pas = gen_pass(15)

print(my_pas)
