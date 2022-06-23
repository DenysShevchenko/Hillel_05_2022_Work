vector = tuple[int, int]


class Vectors:
    @staticmethod
    def add(a: vector, b: vector) -> vector:
        c = (a[0] + b[0], a[1] + b[1])
        return c


a = (5, 7)
b = (2, 9)

c = Vectors.add(a, b)

print(a, b, c)
