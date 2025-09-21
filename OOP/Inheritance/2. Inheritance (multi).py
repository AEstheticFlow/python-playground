# ------------------ 2. MULTILEVEL + MULTIPLE INHERITANCE ------------------ #
# New class hierarchy
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Prey inherits from Animal
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


# Predator inherits from Animal
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# Multilevel: Rabbit inherits from Prey, which inherits from Animal
class Rabbit(Prey):
    pass


# Multilevel: Hawk inherits from Predator, which inherits from Animal
class Hawk(Predator):
    pass


# Multiple Inheritance: Fish inherits from BOTH Prey and Predator
class Fish(Prey, Predator):
    pass

print("-" * 60)
print(f"{'MULTILEVEL + MULTIPLE INHERITANCE DEMO':^59}")
print("-" * 60)

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# Rabbit can eat/sleep (from Animal) + flee (from Prey)
rabbit.eat()
rabbit.flee()

# Hawk can eat/sleep (from Animal) + hunt (from Predator)
hawk.sleep()
hawk.hunt()

# Fish has access to BOTH flee() from Prey and hunt() from Predator
fish.eat()
fish.flee()
fish.hunt()
print("-" * 60)


# https://www.youtube.com/watch?v=Q8YlYHjksLo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=50