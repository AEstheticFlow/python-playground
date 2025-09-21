# Built-in and Math Library Function Demonstration
import math

# Basic numeric variables
x = 3.14
y = -4
z = 5

print(f"Values: x = {x}, y = {y}, z = {z}")
print("-" * 60)

# 1. round()
print("1. Rounding x:")

result1 = round(x)
print(f"round(x) = {result1}")
print("-" * 60)

# 2. abs()
print("2. Absolute value of y:")

result2 = abs(y)
print(f"abs(y) = {result2}")
print("-" * 60)

# 3. pow()
print("3. Power function pow(4, 3):")

result3 = pow(4, 3)
print(f"pow(4, 3) = {result3}")
print("-" * 60)

# 4. max()
print("4. Maximum value among x, y, z:")

result4 = max(x, y, z)
print(f"max(x, y, z) = {result4}")
print("-" * 60)

# 5. min()
print("5. Minimum value among x, y, z:")

result5 = min(x, y, z)
print(f"min(x, y, z) = {result5}")
print("-" * 60)

# ---------------------Using the math library--------------------- #
print("6. Math Library Functions:")

print(f"math.pi = {math.pi:.5f}")   # Rounded to 5 decimal places
print(f"math.e  = {math.e:.5f}")
print("-" * 60)

# 7. math.sqrt()
k = 9.9
print("Value of k =", k)

print("7. Square root of k:")

result6 = math.sqrt(k)
print(f"math.sqrt(k) = {result6}")
print("-" * 60)

# 8. math.ceil()
print("8. Rounding up k (ceil):")

result7 = math.ceil(k)
print(f"math.ceil(k) = {result7}")
print("-" * 60)

# 9. math.floor()
print("9. Rounding down k (floor):")

result8 = math.floor(k)
print(f"math.floor(k) = {result8}")
print("-" * 60)


# https://www.youtube.com/watch?v=jc7TBgMS_kw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=5