# Collections Demonstration
# ---------------------------------------
# List     = [] ordered, changeable, allows duplicates
# Tuple    = () ordered, unchangeable, allows duplicates, faster
# Set      = {} unordered, unindexed, mutable (add/remove), no duplicates

# ------------------ 1. LIST ------------------ #
print("-" * 60)
print("1. LIST=>")
fruits_list = ["apple", "orange", "banana", "coconut"]
print(f"Original list: {fruits_list}")

# Copy
fruits_list_copy = fruits_list.copy()
print(f"Copied list: {fruits_list_copy}")

# Accessing and checking
print("Length:", len(fruits_list))
print("(pineapple) in list?:", "pineapple" in fruits_list)    # Returns True or False

# Modifying
fruits_list[0] = "pineapple"
fruits_list.append("kiwi")
fruits_list.insert(1, "grape")
fruits_list.remove("banana")
fruits_list.sort()                  # Sorts alphabetically
fruits_list.reverse()

# Info
print(f"Modified list: {fruits_list}")
print("Index of (orange):", fruits_list.index("orange"))    # Returns indedx num
print("Count of (kiwi):", fruits_list.count("kiwi"))

# Clearing
fruits_list.clear()
print(f"Cleared list: {fruits_list}")
print("-" * 60)


# ------------------ 2. TUPLE ------------------ #
print("2. TUPLE=>")
fruits_tuple = ("apple", "orange", "banana", "coconut")
print(f"Tuple: {fruits_tuple}")

# Accessing and checking
print("Length:", len(fruits_tuple))
print("(banana) in tuple?", "banana" in fruits_tuple)

# Info (Tuples support only non-mutating methods)
print("Index of (banana):", fruits_tuple.index("banana"))
print("Count of (apple):", fruits_tuple.count("apple"))

# Tuples are immutable; the following would raise errors:
# fruits_tuple[0] = "pineapple"
# fruits_tuple.append("kiwi")
print("-" * 60)

# ------------------ 3. SET ------------------ #
print("3. SET=>")
fruits_set = {"apple", "orange", "banana", "coconut"}
print(f"Original set: {fruits_set}")

# Copy
fruits_set_copy = fruits_set.copy()
print(f"Copied set: {fruits_set_copy}")

# Checking and adding/removing
print("Length:", len(fruits_set))
print("(orange) in set?", "orange" in fruits_set)

fruits_set.add("kiwi")         # Adding an element
fruits_set.remove("apple")     # Removing an element
fruits_set.discard("mango")    # Safe remove (no error if not found)
fruits_set.pop()               # Removes a random element

print(f"Modified set: {fruits_set}")

# Clearing
fruits_set.clear()
print(f"Cleared set: {fruits_set}")
print("-" * 60)


# https://www.youtube.com/watch?v=gOMW_n2-2Mw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=21

# https://www.youtube.com/watch?v=Xy6qeQWQwFw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=23