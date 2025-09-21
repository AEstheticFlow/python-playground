# Type Casting Demonstration
# Type casting = Converting a value from one data type to another
#               Types: str, int, float, bool
#               Can be Explicit (by you) or Implicit (by Python)

name = "Johnathan"
age = 21
gpa = 3.5
student = True

print("-" * 60)
print("Original values and their types:")
print(f"name    = {name}     → {type(name)}")
print(f"age     = {age}         → {type(age)}")
print(f"gpa     = {gpa}        → {type(gpa)}")
print(f"student = {student}   → {type(student)}")
print("-" * 60)

# 1. int → float
print("1. Converting age (int → float):")

age = float(age)
print(f"age (float) = {age} → {type(age)}")
print("-" * 60)

# 2. float → int
print("2. Converting gpa (float → int):")

gpa = int(gpa)
print(f"gpa (int) = {gpa} → {type(gpa)}")
print("-" * 60)

# 3. bool → str
print("3. Converting student (bool → str):")

student = str(student)
print(f"student (str) = {student} → {type(student)}")
print("-" * 60)

# 4. str → bool
print("4. Converting name (str → bool):")

name = bool(name)  # Any non-empty string becomes True, if empty = False
print(f"name (bool) = {name} → {type(name)}")
print("-" * 60)


# ------------------ 5. list(), tuple(), set() Casting ------------------ #
print("5. Converting between collection types:")

example_data = [1, 2, 2, 3]
print("Original list:", example_data, "→", type(example_data))

# list → tuple
as_tuple = tuple(example_data)
print("List to Tuple:", as_tuple, "→", type(as_tuple))

# list → set (removes duplicates)
as_set = set(example_data)
print("List to Set (unique values):", as_set, "→", type(as_set))

# set → list
back_to_list = list(as_set)
print("Set back to List:", back_to_list, "→", type(back_to_list))

# tuple → set
from_tuple = set(as_tuple)
print("Tuple to Set:", from_tuple, "→", type(from_tuple))

# set → tuple
to_tuple = tuple(from_tuple)
print("Set to Tuple:", to_tuple, "→", type(to_tuple))

print("-" * 60)


# https://www.youtube.com/watch?v=Qtq83lAoogM&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=3