# Iterables Demonstration
# -------------------------------------
# Iterable = An object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop.
# Common examples: list, tuple, set, string, dictionary

# ------------------ 1. CREATE ITERABLES ------------------
my_list = [1, 2, 3, 4, 5]                  # List → Ordered, changeable, reversible
my_tuple = (1, 2, 3, 4, 5)                 # Tuple → Ordered, unchangeable, reversible
my_set = {"apple", "orange", "banana"}     # Set → Unordered, no duplicates, not reversible
my_string = "Mo Salah"                     # String → Ordered, reversible
my_dictionary = {'A': 1, 'B': 2, 'C': 3}   # Dict → Key-value pairs, ordered (3.7+)

# ------------------ 2. LOOPING OVER A LIST ------------------
print("List iteration (reversible):")
for item in my_list:
    print(item, end=" ")
print("\nReversed list:")
for item in reversed(my_list):
    print(item, end=" ")
print("\n" + "-" * 60)

# ------------------ 3. LOOPING OVER A TUPLE ------------------
print("Tuple iteration (reversible):")
for item in my_tuple:
    print(item, end=" ")
print("\nReversed tuple:")
for item in reversed(my_tuple):
    print(item, end=" ")
print("\n" + "-" * 60)

# ------------------ 4. LOOPING OVER A SET ------------------
print("Set iteration (unordered, not reversible), random different result every time:")
for item in my_set:
    print(item, end=" ")
print("\n" + "-" * 60)

# ------------------ 5. LOOPING OVER A STRING ------------------
print("String iteration (reversible):")
for char in my_string:
    print(char, end=" ")
print("\nReversed string:")
for char in reversed(my_string):
    print(char, end=" ")
print("\n" + "-" * 60)

# ------------------ 6. LOOPING OVER A DICTIONARY ------------------
print("Dictionary iteration (keys):")
for key in my_dictionary:
    print(key, end=" ")
print("\n" + "-" * 60)

print("Dictionary iteration (values):")
for value in my_dictionary.values():
    print(value, end=" ")
print("\n" + "-" * 60)

print("Dictionary iteration (key-value pairs):")
for key, value in my_dictionary.items():
    print(f"{key} = {value}")
print("-" * 60)


# https://www.youtube.com/watch?v=VL_g3LjsFqs&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=36