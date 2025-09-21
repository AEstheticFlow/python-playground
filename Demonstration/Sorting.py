"""
Python Sorting:
1. Sorting Lists
2. Sorting Tuples
3. Sorting Dictionaries
4. Sorting Objects
"""

# ---------------------------------------------------------------------------
# 1. SORTING LISTS
# ---------------------------------------------------------------------------

fruits = ["banana", "orange", "apple", "coconut"]

print('-' * 100)
print("Original list:", fruits)

# Sort alphabetically (A-Z)
fruits.sort()
print("Sorted (A-Z):", fruits)

# Sort in reverse (Z-A)
fruits.sort(reverse=True)
print("Sorted (Z-A):", fruits)
print('-' * 100)

# ---------------------------------------------------------------------------
# 2. SORTING TUPLES
# ---------------------------------------------------------------------------

fruits_tuple = ("banana", "orange", "apple", "coconut")
print("Original tuple:", fruits_tuple)

# Convert to sorted tuple (A-Z)
fruits_tuple = tuple(sorted(fruits_tuple))
print("Sorted tuple (A-Z):", fruits_tuple)

# Convert to sorted tuple (Z-A)
fruits_tuple = tuple(sorted(fruits_tuple, reverse=True))
print("Sorted tuple (Z-A):", fruits_tuple)
print('-' * 100)

# ---------------------------------------------------------------------------
# 3. SORTING DICTIONARIES
# ---------------------------------------------------------------------------

fruits_dict = {
    "banana": 105,
    "apple": 72,
    "orange": 73,
    "coconut": 354
}
print("Original dict:", fruits_dict)

# Sort by KEYS (A-Z)
by_key = dict(sorted(fruits_dict.items()))
print("Sorted by KEYS (A-Z):", by_key)

# Sort by KEYS (Z-A)                                          # item[0] = key
by_key_desc = dict(sorted(fruits_dict.items(), key=lambda item: item[0], reverse=True))
print("Sorted by KEYS (Z-A):", by_key_desc)

# Sort by VALUES (low to high)                             # item[1] = value
by_value = dict(sorted(fruits_dict.items(), key=lambda item: item[1]))
print("Sorted by VALUES (low-high):", by_value)

# Sort by VALUES (high to low)
by_value_desc = dict(sorted(fruits_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by VALUES (high-low):", by_value_desc)
print('-' * 100)


# ---------------------------------------------------------------------------
# 4. SORTING OBJECTS
# ---------------------------------------------------------------------------

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits_objects = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]

print("Original objects:", fruits_objects)

# Sort objects by NAME (A-Z)
by_name = sorted(fruits_objects, key=lambda fruit: fruit.name)
print("Sorted objects by NAME (A-Z):", by_name)

# Sort objects by NAME (Z-A)
by_name_desc = sorted(fruits_objects, key=lambda fruit: fruit.name, reverse=True)
print("Sorted objects by NAME (Z-A):", by_name_desc)

# Sort objects by CALORIES (low-high)
by_calories = sorted(fruits_objects, key=lambda fruit: fruit.calories)
print("Sorted objects by CALORIES (low-high):", by_calories)

# Sort objects by CALORIES (high-low)
by_calories_desc = sorted(fruits_objects, key=lambda fruit: fruit.calories, reverse=True)
print("Sorted objects by CALORIES (high-low):", by_calories_desc)
print('-' * 100)


# https://www.youtube.com/watch?v=cd-vtiO5chk&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=67