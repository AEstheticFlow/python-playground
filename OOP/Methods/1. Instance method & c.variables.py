# Classes Demonstration

# ------------------ 1. CAR CLASS ------------------ #
class Car:
    def __init__(self, model, year, color, for_sale):       # Constructor
        # 'Instance variables' (unique to each object)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods
    def drive(self):
        print(f"{self.model} is driving")

    def stop(self):
        print(f"{self.model} is stopping")

    def describe(self):
        print(f"{self.model} is a {self.year}, {self.color} car. "
              f"For sale? {self.for_sale}")
# ******************************************************************** #

# Create car objects
car1 = Car("Mustang", 2023, "Black", True)
car2 = Car("Ford", 2024, "Red", False)
car3 = Car("Charger", 2025, "White", True)

# Demonstrate functionality
print("-" * 60)
print(f"{'CAR OBJECTS DEMO':^58}")
print("-" * 60)

'''car1.drive()
   car1.stop()
   car1.describe()
   print("-" * 60)

   car2.drive()
   car2.stop()
   car2.describe()
   print("-" * 60)

   car3.drive()
   car3.stop()
   car3.describe()
   print("-" * 60)'''

# Better:
for car in (car1, car2, car3):          # Tuple of objects, iterable 
    car.drive()
    car.stop()
    car.describe()
    print("*" * 60)


# ------------------ 2. STUDENT CLASS ------------------ #
class Student:

    # 'Class variables'    (shared by ALL objects of this class)
    class_year = 2025      # One graduating year for the whole group
    num_students = 0       # Counter shared among all students

    def __init__(self, name, age):
        # 'Instance variables' (unique to each student)
        self.name = name
        self.age = age
        Student.num_students += 1       # Update shared variable: increments once per new Student created

    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old.")


# Create student objects
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# Demonstrate functionality
print("-" * 60)
print(f"{'STUDENT OBJECTS DEMO':^56}")
print("-" * 60)

for student in (student1, student2, student3, student4):      # Tuple of objects, iterable
    student.introduce()

# Accessing shared variables
print("\n--- Shared Variables Explained ---")
print(f"Graduating class year (shared): {Student.class_year}")
print(f"Total students (shared counter): {Student.num_students}")

# IMPORTANT: Access shared variables via the CLASS, not the object
# Good:   Student.num_students
# Bad:    student1.num_students   (still works, but confusing!)
print("-" * 60)


# https://www.youtube.com/watch?v=1XE-_s4ZBT8&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=47

# https://www.youtube.com/watch?v=bytvWg4fPB0&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=48