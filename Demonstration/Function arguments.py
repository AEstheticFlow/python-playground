# Function Parameters Demonstration
# -----------------------------------------------
# 1. Positional Arguments   → Order matters
# 2. Default Arguments      → Use default if no value is provided
# 3. Keyword Arguments      → Order doesn't matter if you name them
# 4. Arbitrary Arguments    → Allow variable number of arguments (*args, **kwargs)


# ------------------ 1. POSITIONAL ------------------ #
print("1. POSITIONAL ARGUMENTS:")
def greet_positional(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

# Order matters:
greet_positional("John", "Doe")
greet_positional("Doe", "John")  # Totally different meaning!
print("-" * 60)


# ------------------ 2. DEFAULT ------------------ #
print("2. DEFAULT ARGUMENTS:")
def greet_default(first_name="John", last_name="Doe"):
    print(f"Hello {first_name} {last_name}!")

# Can skip parameters if you’re okay with defaults:
greet_default()
greet_default("Alice")
greet_default("Alice", "Smith")
print("-" * 60)


# ------------------ 3. KEYWORD ------------------ #
print("3. KEYWORD ARGUMENTS:")
def greet_keyword(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

# Order doesn't matter if you name them:
greet_keyword(last_name="Wayne", first_name="Bruce")
print("-" * 60)


# ------------------ 4. ARBITRARY ------------------ #
print("4. ARBITRARY ARGUMENTS:")
# *args → arbitrary number of 'positional' arguments (tuple)
def add_numbers(*args):
    total = sum(args)
    print(f"Sum of {args} = {total}")

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)
print()

# **kwargs → arbitrary number of keyword arguments (dict)
def get_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    

get_info(name="Alice", age=30, city="New York")       # Keywords = keys
print()

# Using both *args and **kwargs →
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
        
    print("\nKeys:")
    for key in kwargs.keys():
        print(key, end=" ")
        
    print("\nValues:")
    for value in kwargs.values():
        print(value, end=" ")
    print()

shipping_label("Mr.", "Spongebob", "Squarepants", "III",
               street="123 street.",apt="4", city="Housten", state="Texas", zip="54321")

print("-" * 60)


# https://www.youtube.com/watch?v=m2uURZxex3c&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=33

# https://www.youtube.com/watch?v=7QCHpAtlSMo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=34

# https://www.youtube.com/watch?v=Vh__2V2tXUM&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=35