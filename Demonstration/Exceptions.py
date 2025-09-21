"""
Python Exceptions:
1. Basic try-except-finally
2. Common built-in exceptions (ZeroDivisionError, ValueError, IndexError, KeyError, FileNotFoundError)
3. Custom exceptions (user-defined)
"""

# ---------------------------------------------------------------------------
# 1. BASIC TRY-EXCEPT-FINALLY
# ---------------------------------------------------------------------------

try:
    number = int(input("Enter a number: "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:      # Entered a string for example
    print("Please enter a valid number!")

except Exception:
    # This is a broad catch-all; use sparingly
    print("Something unexpected went wrong!")

finally:
    print("**This always runs (cleanup, close files, release resources, etc.)\n")


# ---------------------------------------------------------------------------
# 2. COMMON BUILT-IN EXCEPTIONS
# ---------------------------------------------------------------------------

# IndexError
try:
    items = [1, 2, 2]
    print(items[5])     # index out of range
except IndexError:
    print("IndexError: Tried to access a list index that doesn't exist.")

# KeyError
try:
    data = {"name": "Bob"}
    print(data["age"])      # key doesn't exist
except KeyError:
    print("KeyError: The specified key is missing in the dictionary.")

# FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError: The file you're trying to read doesn't exist.")

print("**Common built-in exceptions block finished.\n")


# ---------------------------------------------------------------------------
# 3. CUSTOM EXCEPTIONS
# ---------------------------------------------------------------------------

class NegativeNumberError(Exception):
    """Custom exception for handling negative numbers."""
    pass

def process_number(num):
    # Validate input: raise custom exception if number is negative
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"Processed number: {num}"  # Return processed result if valid

try:
    user_number = int(input("Enter a positive number: "))  
    result = process_number(user_number)                   # Validate & process
    print(result)                                          

except NegativeNumberError as e:
    # Handle custom exception with a clear message
    print(f"Custom Exception Triggered: {e}")

print("**Custom exception block finished.\n")  # Always runs at the end


# ---------------------------------------------------------------------------
# Recap:
# ---------------------------------------------------------------------------
# - Always catch specific exceptions first (ZeroDivisionError, ValueError, etc.).
# - Use finally for guaranteed cleanup.
# - Create custom exceptions for domain-specific errors (like NegativeNumberError).


# https://www.youtube.com/watch?v=V_NXT2-QIlE&t=1s