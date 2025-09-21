"""
Python Functional Programming
1. Lambda Functions
2. map()
3. filter()
4. reduce()
"""

# ---------------------------------------------------------------------------
# 1. LAMBDA FUNCTIONS
# ---------------------------------------------------------------------------
# Lambda = small, anonymous, single-use ("throwaway") functions.
# Syntax: lambda parameters: expression
# Useful with higher-order functions (map, filter, reduce) to keep code concise.

# Examples:
double = lambda x: x * 2                            # Doubles a number
add = lambda x, y: x + y                            # Adds two numbers
max_value = lambda x, y: x if x > y else y          # Returns greater of two values
min_value = lambda x, y: x if x < y else y          # Returns smaller of two values
full_name = lambda first, last: first + " " + last  # Joins first and last name
is_even = lambda x: x % 2 == 0                      # Checks if a number is even
age_check = lambda age: age >= 18                   # Checks if age is adult

# Test lambda functions:
print(double(2))                               # 4
print(add(3, 4))                               # 7
print(max_value(6, 7))                         # 7
print(min_value(9, 8))                         # 8
print(full_name("Spongebob", "Squarepants"))   # Spongebob Squarepants
print(is_even(5))                              # False
print(age_check(21))                           # True


# ---------------------------------------------------------------------------
# 2. map(function, collection)
# ---------------------------------------------------------------------------
# Applies a given function to ALL items in an iterable.
# Syntax: map(function, iterable) -> returns a map object (convert to list for display).

# Example using a regular function:
def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
fahrenheit_temps = list(map(c_to_f, celsius_temps))
print(fahrenheit_temps)         # [32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

# Example using a lambda function:
fahrenheit_temps = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)


# ---------------------------------------------------------------------------
# 3. filter(function, collection)
# ---------------------------------------------------------------------------
# Filters elements based on a CONDITION.
# Syntax: filter(function, iterable) -> returns filter object (convert to list).

# Example using a regular function:
def is_passing(grade):
    return grade >= 60

grades = [91, 32, 83, 44, 75, 56, 67]
passing_grades = list(filter(is_passing, grades))
print(passing_grades)           # [91, 83, 75, 67]

# Example using a lambda function:
passing_grades = list(filter(lambda grade: grade >= 60, grades))
print(passing_grades)


# ---------------------------------------------------------------------------
# 4. reduce(function, collection)
# ---------------------------------------------------------------------------
# Reduces a collection to a SINGLE cumulative value.
# Requires: from functools import reduce
# Syntax: reduce(function, iterable)
# Best for functional style solutions, though loops are often simpler.

from functools import reduce    # Must be imported

# Example using a regular function:
def add(x, y):
    return x + y

prices = [19.99, 1.00, 5.75, 12.99, 10.99]
total = reduce(add, prices)
print(f"${total}")          # $50.72

# Example using a lambda function:
total = reduce(lambda x, y: x + y, prices)
print(f"${total}")          # $50.72


# ---------------------------------------------------------------------------
# Recap Notes:
# ---------------------------------------------------------------------------
# 1. Lambda is for quick, inline functions (often with map/filter/reduce).
# 2. map() transforms each element.
# 3. filter() selects certain elements.
# 4. reduce() accumulates everything into one result.
# 5. Combining these = concise functional programming in Python.


# https://www.youtube.com/watch?v=IljPHDyBRog&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=63

# https://www.youtube.com/watch?v=OXfcmRFne0Q&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=64

# https://www.youtube.com/watch?v=kosZevWurtE&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=65

# https://www.youtube.com/watch?v=mH_hLmZs1h8&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=66