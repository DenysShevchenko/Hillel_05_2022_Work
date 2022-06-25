from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        print('its work')
        pass


class Rectangle(Shape):
    @abstractclassmethod
    def paint(self):
        return"""
                 class Rectangle
                 ----
                 |  |
                 ----
                 """


class Circle(Shape):
    @abstractclassmethod
    def paint(self):
        return"""
                class Circle
                 --
                -  -
                 --
                 """


def get_shape():
    options: list[Shape] = [Rectangle, Circle]
    return choice(options)


def main():

    shape: Shape = get_shape()
    print(shape.paint())
    shape.draw()


if __name__ == "__main__":
    main()
