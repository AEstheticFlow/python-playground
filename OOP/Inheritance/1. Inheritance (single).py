# Inheritance Demonstration
# ------------------------------------------------------
# Inheritance = Allows a class to inherit attributes and methods from another class
# Benefits: code reusability + extensibility
# Syntax: class Child(Parent)


# ------------------ 1. SINGLE INHERITANCE ------------------ #
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True   # Shared by all animals

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Subclasses inherit from Animal
class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")


print("-" * 60)
print(f"{'SINGLE INHERITANCE DEMO':^58}")
print("-" * 60)

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.eat()
dog.speak()
cat.sleep()
cat.speak()
mouse.eat()
mouse.speak()
print("-" * 60)


# https://www.youtube.com/watch?v=u1be7Vele5o&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=49