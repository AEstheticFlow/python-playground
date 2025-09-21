# Membership operators in Python:
#   - `in`     → checks if a value exists in a sequence
#   - `not in` → checks if a value does NOT exist
# Work with: strings, lists, tuples, sets, dictionaries

# --------------------
# EXAMPLE 1: Checking membership in a string
# --------------------
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


# --------------------
# EXAMPLE 2: Checking membership in a set
# --------------------
students = {"Spongebob", "Patrick", "Sandy"}   # sets are unordered collections, unique values only
student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is in this class")
else:
    print(f"{student} is NOT in this class")


# --------------------
# EXAMPLE 3: Checking keys in a dictionary
# --------------------
grades = {
    "Sandy": 'A',
    "Squidward": 'B',
    "Spongebob": 'C',
    "Patrick": 'D'
}

student = input("Enter the name of a student: ")

# `in` checks if the KEY exists (not the value)
if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} is not in the dictionary")


# --------------------
# EXAMPLE 4: Validating a string format
# --------------------
email = "BroCode@gmail.com"

# Simple membership check for '@' and '.' in the string
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# --------------------
# EXAMPLE 5: Using 'not in'
# --------------------
banned_users = ["admin", "root", "test"]

username = input("Choose a username: ")

if username not in banned_users:
    print(f"Username '{username}' is available")
else:
    print(f"Username '{username}' is not allowed")


# https://www.youtube.com/watch?v=OJ5E7VLsZQM&lc=Ugx5-fiChSD0DMNPvzJ4AaABAg