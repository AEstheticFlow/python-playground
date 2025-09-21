# super() Demonstration
# --------------------------------------------------
# super() = Used in a child class to call methods 
#           from a parent class (superclass).
#           Lets child classes EXTEND parent functionality.


# ------------------ PARENT CLASS ------------------ #
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        # Base description shared by ALL shapes
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# ------------------ CHILD CLASSES ------------------ #
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # Call parent constructor
        super().__init__(color, is_filled)
        self.radius = radius

    # Overrides
    def describe(self):
        # Add Circle-specific info, then call parent
        print(f"It is a circle with an area of {3.14 * self.radius ** 2:.2f} cm²")
        super().describe()              # Extending functionality


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width ** 2} cm²")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height) / 2} cm²")
        super().describe()


# ------------------ DEMONSTRATION ------------------ #
print("-" * 60)
circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
print("-" * 60)
square.describe()
print("-" * 60)
triangle.describe()
print("-" * 60)


# https://www.youtube.com/watch?v=HzyhmZqiaE8&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=52