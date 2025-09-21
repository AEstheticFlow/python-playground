# -----------------------------
# DECORATORS
# -----------------------------
# A decorator is a function that:
# 1. Takes another function as an argument.
# 2. Extends/modifies its behavior without changing its original code.
# 3. Returns a new function (usually called "wrapper").

# Why use decorators?
# - Code reuse: Add common behavior (like logging, authentication, validation)
# - Clean, readable, and DRY (Don't Repeat myself)


# Decorator 1: Adds sprinkles to any dessert
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")      # Extra behavior
        func(*args, **kwargs)                # Call the original function
    return wrapper

# Decorator 2: Adds fudge to any dessert
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")        # Extra behavior
        func(*args, **kwargs)              # Call the original function
    return wrapper
# -------------------------------------------------------------------------- #

@add_sprinkles  # Outer decorator
@add_fudge      # Inner decorator
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

# Function Call:
get_ice_cream("vanilla")

# NOTE: I use *args and **kwargs to be able to accept any kind of arguments


# https://www.youtube.com/watch?v=U-G-mSd4KAE&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=62
