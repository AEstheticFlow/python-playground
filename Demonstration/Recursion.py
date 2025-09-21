"""
Python Recursion:
1. Concept of Recursion vs. Iteration
2. Example: Walking steps
3. Example: Factorial calculation
"""

# ---------------------------------------------------------------------------
#   RECURSION CONCEPT
# ---------------------------------------------------------------------------
# Recursion = A function calling itself from within.
# Iteration = Using loops.
# Iterative solutions are usually faster.
# Recursive solutions are often simpler to write & understand.


# ---------------------------------------------------------------------------
#    EXAMPLE 1 – WALKING STEPS
# ---------------------------------------------------------------------------

# Iterative approach:
def walk_iterative(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{step}")

print("Iterative walk:")
walk_iterative(10)

print('-' * 25)

# Recursive approach:
def walk_recursive(steps):
    if steps == 0:
        return                  # returns None, just stops recursion
    walk_recursive(steps - 1)
    print(f"You take step #{steps}")

print("Recursive walk:")
walk_recursive(10)
print()


# ---------------------------------------------------------------------------
#    EXAMPLE 2 – FACTORIAL
# ---------------------------------------------------------------------------

# Iterative approach:
def factorial_iterative(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print("Iterative factorial of 10:")
print(factorial_iterative(10))

print('-' * 25)

# Recursive approach:
def factorial_recursive(x):
    if x == 1:
        return 1
    return x * factorial_recursive(x - 1)

print("Recursive factorial of 10:")
print(factorial_recursive(10))


# https://www.youtube.com/watch?v=ivl5-snqul8&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=68