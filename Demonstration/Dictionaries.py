# Dictionary Demonstration 
# --------------------------------------
# Dictionary = { key: value } pairs, possibly in different data types
#   Ordered (Python 3.7+)
#   Changeable
#   No duplicate keys allowed

# ------------------ 1. CREATE ------------------ #
print("-" * 60)
print("1. Creating a dictionary of countries and capitals:")

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(f"Original dictionary: {capitals}")
print("Accessing one value using its key:", capitals["USA"])
print("-" * 60)

# ------------------ 2. ACCESS ------------------ #
print("2. Accessing values with .get():")   
# Safer way to access values than just: capitals["Japan"], which causes a KeyError 

print("Capital of Russia:", capitals.get("Russia"))
print("Capital of Japan (not found):", capitals.get("Japan"))  # Returns None
print("-" * 60)

# ------------------ 3. ADD / UPDATE ------------------ #
print("3. Adding and updating values:")

capitals.update({"Germany": "Berlin"})       # Add new entry
capitals.update({"USA": "Detroit"})          # Update existing entry
print(f"After update: {capitals}")
print("-" * 60)

# ------------------ 4. REMOVE ------------------ #
print("4. Removing entries:")

capitals.pop("China")                        # Remove by key
print(f"After popping (China): {capitals}")

removed_item = capitals.popitem()            # Remove last inserted key-value pair
print(f"Removed last item: {removed_item}")
print(f"After popitem(): {capitals}")
print("-" * 60)

# ------------------ 5. INSPECT ------------------ #
print("5. Inspecting keys and values:")

print("Keys:", list(capitals.keys()))       
print("Values:", list(capitals.values()))   
print("Items:", list(capitals.items()))     
print("-" * 60)

# ------------------ 6. LOOPING ------------------ #
print("6. Looping through dictionary items:")

for country, capital in capitals.items():
    print(f"{country}: {capital}")
print("-" * 60)

# ------------------ 7. CLEAR ------------------ #
print("7. Clearing the dictionary:")

capitals.clear()
print(f"After clear(): {capitals}")
print("-" * 60)


# https://www.youtube.com/watch?v=MZZSMaEAC2g&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=25