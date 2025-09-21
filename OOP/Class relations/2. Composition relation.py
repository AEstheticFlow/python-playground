# 2. Composition = "Owns-A" relationship
#   - The containing object directly creates and owns its parts
#   - The parts (objects) cannot exist independently of the whole


# Independent parts (engine, wheels) created INSIDE Car
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size


# COMPOSITION: Car *owns* Engine and Wheels
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # Engine and Wheels are CREATED within Car, not passed in
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]  # Always 4 wheels

    def display_car(self):
        return f"{self.make} {self.model}, {self.engine.horse_power} H.P, {self.wheels[0].wheel_size}-inch wheels"
# --------------------------------------------------------------------------------------- #

# Create cars → engine/wheels don't exist outside of them
car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print('-' * 40)
print(car2.display_car())

# In aggregation (Library/Book example), the Book existed independently of Library.
# In composition (this Car example), the Engine and Wheels do not exist without the Car — they’re created inside it.
# If I del car1, its engine and wheels are gone too. That’s the hallmark of composition.


# https://www.youtube.com/watch?v=TPUdUkFHD5I&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=56