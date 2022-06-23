from __future__ import annotations


class Test:
    def __new__(cls) -> Test:
        instance = super().__new__(cls)
        return instance

    def __init__(self) -> None:
        self.attribute = "Value"

    @classmethod
    def greeting(cls) -> None:
        name = cls.get_name()

        print(f"Hello {name}")

    @classmethod
    def get_name(cls) -> str:
        return "Dima"

    def __str__(self) -> str:
        return self.get_name()


instance: Test = Test()
# instance.greeting()

# Test.greeting()
# print(instance.__str__())
print(instance)
