import math


class Shape:
    def area(self):
        return 0

    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f"Drawing a rectangle {self.width}x{self.height}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print(f"Drawing a triangle with base {self.base} and height {self.height}")


if __name__ == "__main__":
    shapes = [
        Circle(3),
        Rectangle(4, 5),
        Triangle(6, 2)
    ]

    for shape in shapes:
        shape.draw()
        print(f"Area: {shape.area():.2f}\n")
