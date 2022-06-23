class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        instance = Vector(x=(self.x + other.x), y=(self.y + other.y))
        return instance

    def __sub__(self, other: "Vector") -> "Vector":
        instance = Vector(x=(self.x - other.x), y=(self.y - other.y))
        return instance

    def __mul__(self, other: "Vector") -> "Vector":
        instance = Vector(x=(self.x * other.x), y=(self.y * other.y))
        return instance

    def __truediv__(self, other: "Vector") -> "Vector":
        instance = Vector(x=(self.x // other.x), y=(self.y // other.y))
        return instance

    def __floordiv__(self, other: "Vector") -> "Vector":
        return self.__truediv__(other)


a = Vector(10, 20)
b = Vector(4, 13)

c = a + b
# c = a.__add__(b)
# c = Vector.__add__(a, b)

# var_name = str(c)
# var_name = c.__str__()

d = a - b
e = a * b
k = a / b

print(a, b)
print(c)
print(d)
print(e)
print(k)
