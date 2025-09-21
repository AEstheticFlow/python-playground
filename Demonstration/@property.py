# ---------- @property Decorator ----------
# @property = Treats a method like an attribute (getter)
# Benefits:
# 1. Add validation or logic when reading, writing, or deleting attributes
# 2. Encapsulates "private" attributes (convention: _attribute)
# 3. Keeps my class interface clean and Pythonic
#
# Components:
#   - @property         → Getter (read attribute)
#   - @<prop>.setter    → Setter (modify attribute)
#   - @<prop>.deleter   → Deleter (delete attribute)

class Rectangle:
    def __init__(self, width, height):
        # Using leading underscore to indicate "private" variables
        self._width = width
        self._height = height

    # ---------- GETTERS ----------
    @property
    def width(self):
        """Returns formatted width"""
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        """Returns formatted height"""
        return f"{self._height:.1f} cm"

    @property
    def area(self):
        """Computed property (width * height)"""
        return f"Area: {self._width * self._height:.1f} cm²"

    # ---------- SETTERS ----------
    @width.setter
    def width(self, value):
        """Validates and sets width"""
        if value > 0:
            self._width = value
        else:
            print("❌ Width must be greater than zero")

    @height.setter
    def height(self, value):
        """Validates and sets height"""
        if value > 0:
            self._height = value
        else:
            print("❌ Height must be greater than zero")

    # ---------- DELETERS ----------
    @width.deleter
    def width(self):
        """Deletes width attribute"""
        del self._width
        print("Width has been deleted ✅")

    @height.deleter
    def height(self):
        """Deletes height attribute"""
        del self._height
        print("Height has been deleted ✅")


# ---------- EXAMPLE USAGE ----------
rectangle = Rectangle(3, 4)

# Access like attributes (but with validation/logic inside)
print(rectangle.width)    # Getter for width
print(rectangle.height)   # Getter for height
print(rectangle.area)     # Computed property

# Modify values with validation
rectangle.width = 5
rectangle.height = -2      # Invalid, triggers validation

print(rectangle.width)
print(rectangle.height)     # Won't change
print(rectangle.area)

# Delete attributes
del rectangle.width
del rectangle.height


# NOTE: I *can* access _width and _height directly since Python does not enforce strict private attributes.
#       However, this bypasses the validation logic in the @property setters, risking invalid values.
#       Example:
#           rectangle._width = -5  # No error, but object state becomes invalid!
#       Best practice: Always use the property (rectangle.width) to ensure validation and consistent state.


# https://www.youtube.com/watch?v=HkbQ_NaH0Lc&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=61