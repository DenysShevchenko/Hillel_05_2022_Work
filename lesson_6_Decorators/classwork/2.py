def greeting(message):
    def wrapper(func):
        def inner():
            print(message)
            return func()

        return inner

    return wrapper


@greeting("Hello Dima!")
def dima():
    return "my name is Dima"


@greeting("Hello Vania!")
def vania():
    return "my name is Vania"


# greeting_dima = greeting(dima)()
print(dima())
print(vania())
