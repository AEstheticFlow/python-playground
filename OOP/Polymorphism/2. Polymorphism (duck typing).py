# 2. DUCK TYPING
# ------------------------------
# In Python, what matters is not the *type* of the object, but whether 
# it has the required attributes/methods.

# Principle: "If it looks like a duck and quacks like a duck, it must be a duck."


class Animal:
    alive = True   # shared attribute across all "living" things


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False   # Not really an Animal, but still shares the same attribute

    def speak(self):
        print("HONK!")

# Notice: Car is *not* inheriting from Animal,
# yet it behaves like one because it has both 'alive' and 'speak'.
# This is "duck typing" in action.

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()                   # polymorphic: each "animal" knows how to speak
    print(f"Alive? {animal.alive}")  # Car also has 'alive', so it works too
    print("-" * 30)


# https://www.youtube.com/watch?v=Qe03kCuTMoU&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=54