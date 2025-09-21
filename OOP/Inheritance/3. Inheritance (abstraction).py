# Abstract class: A class that cannot be instantiated on its own; meant to be subclassed.
#                 They can contain abstract methods, which are declared but not implemented.
# 
# Abstract classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Forces child classes to implement required abstract methods
# ---------------------------------------------------------------

from abc import ABC, abstractmethod

# ---------------- Base Abstract Class ---------------- #
class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        """Abstract method: Must be implemented by subclass"""
        pass

    @abstractmethod
    def stop(self):
        """Abstract method: Must be implemented by subclass"""
        pass


# ---------------- Subclasses ---------------- #
class Car(Vehicle):
    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def drive(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    def drive(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


# ---------------- Demonstration ---------------- #
car = Car()
car.drive()
car.stop()
print("-" * 50)

motorcycle = Motorcycle()
motorcycle.drive()
motorcycle.stop()
print("-" * 50)

boat = Boat()
boat.drive()
boat.stop()
print("-" * 50)

# 🚫 If you try this, Python will throw an error:
# vehicle = Vehicle()
# TypeError: Can't instantiate abstract class Vehicle with abstract methods drive, stop


# https://www.youtube.com/watch?v=97V7ICVeTJc&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=51