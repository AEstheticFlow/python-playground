# ---------- main.py ---------- #
# Demonstration of importing and using a custom Python module

# ------------------ 1. IMPORT ------------------
import exampleModule

# ------------------ 2. USING MODULE CONTENT ------------------
print("-" * 60)
print("Accessing constants and functions from (exampleModule.py):")

# Constant
result1 = exampleModule.pi
print(f"Value of pi: {result1}")

# Functions
result2 = exampleModule.square(3)
print(f"Square of 3: {result2}")

result3 = exampleModule.cube(3)
print(f"Cube of 3: {result3}")

result4 = exampleModule.circumference(3)
print(f"Circumference of circle (r=3): {result4}")

result5 = exampleModule.area(3)
print(f"Area of circle (r=3): {result5}")
print("-" * 60)

# ------------------ 3. SUMMARY ------------------
print("Summary dictionary of results:")
results_summary = {
    "pi": result1,
    "square(3)": result2,
    "cube(3)": result3,
    "circumference(3)": result4,
    "area(3)": result5
}
for name, value in results_summary.items():
    print(f"{name:16} = {value}")


# https://www.youtube.com/watch?v=XcfxkHrHTVE&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=40