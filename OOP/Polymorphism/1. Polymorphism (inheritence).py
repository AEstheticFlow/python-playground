# Polymorphism = "many forms or faces"
# ------------------------------------------------------------
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = Objects of different subclasses 
#                  can be treated as if they are of the same parent type.
# ------------------------------------------------------------

from abc import ABC, abstractmethod

# ---------------- Base Abstract Class ---------------- #
class Shape(ABC):

    @abstractmethod
    def area(self):
        """Every shape must define how to calculate its area"""
        pass


# ---------------- Subclasses ---------------- #
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# A Pizza *is a Circle* but adds extra attributes
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

    def describe(self):
        return f"A {self.topping} pizza with area {self.area()}cm²"


# ---------------- Demonstration ---------------- #
# One iterable objects contains all classes
shapes = [  
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza("pepperoni", 15),
]

# Polymorphism in action:
# Even though these are different classes, 
# we can treat them all as `Shape` and call `.area()` uniformly.
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}cm²")
print()

# Demonstrating Pizza’s extended functionality
print(shapes[-1].describe())


# https://www.youtube.com/watch?v=tHN8I_4FIt8&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=53