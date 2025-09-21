# String Methods Demonstration 

print("-" * 50)
name = "Johnathan"
phone_number = "123-456-7890"

print(f"Original name: {name}")
print(f"Original phone_number: {phone_number}")
print("-" * 50)

# 1. len(name)
print("1. Length of the name:")

print("len(name) =", len(name))  # Counts characters
print("-" * 50)

# 2. name.find()
print("2. Finding a character or substring in name using .find():")

print("name.find('a') =", name.find('a'))  # Returns first index of 'a'
print("name.find('z') =", name.find('z'))  # Returns -1 if not found
print("-" * 50)

# 3. name.rfind()
print("3. Finding last occurrence of a character using .rfind():")

print("name.rfind('a') =", name.rfind('a'))  # Returns last index of 'a'
print("-" * 50)

# 4. name.capitalize()
print("4. Capitalizing the name:")

print("name.capitalize() =", name.capitalize())  # First letter uppercase, rest lowercase
print("-" * 50)

# 5. name.upper()
print("5. Making name uppercase:")

print("name.upper() =", name.upper())  # All letters uppercase
print("-" * 50)

# 6. name.lower()
print("6. Making name lowercase:")

print("name.lower() =", name.lower())  # All letters lowercase
print("-" * 50)

# 7. name.isdigit()
print("7. Checking if name is all digits:")

print("name.isdigit() =", name.isdigit())  # False, since it's letters
print("-" * 50)

# 8. name.isalpha()
print("8. Checking if name contains only letters:")

print("name.isalpha() =", name.isalpha())  # True if only letters
print("-" * 50)

# 9. phone_number.count()
print("9. Counting how many dashes (-) in phone_number:")

print("phone_number.count('-') =", phone_number.count('-'))  # Count of '-'
print("-" * 50)

# 10. phone_number.replace()
print("10. Replacing dashes with spaces in phone_number:")

print("phone_number.replace('-', ' ') =", phone_number.replace('-', ' '))  # Replace '-' with ' '
print("-" * 50)


# https://www.youtube.com/watch?v=tb6EYiHtcXU&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=12