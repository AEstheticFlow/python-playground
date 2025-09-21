# Indexing Demonstration
# Format: sequence[start : end : step]

credit_number = "1234-5678-9012-3456"

print("-" * 50)
print(f"Original credit card number: {credit_number}")
print("-" * 50)

# 1. Basic indexing
print("1. Accessing a single character:")
print("credit_number[0] =", credit_number[0])  # First character
print("-" * 50)

# 2. Slicing with start and end
print("2. Slicing from index 0 to 4 (exclusive):")
print("credit_number[0:4] =", credit_number[0:4])
print("credit_number[:4]  =", credit_number[:4])  # Same result
print("-" * 50)

# 3. Slicing from a middle index to near end
print("3. Slicing from index 4 to 19:")
print("credit_number[4:19] =", credit_number[4:19])
print("credit_number[4:]   =", credit_number[4:])  # From index 4 to end
print("-" * 50)

# 4. Negative indexing
print("4. Accessing from the end using negative index:")
print("credit_number[-1] =", credit_number[-1])  # Last character
print("credit_number[-4:] =", credit_number[-4:])  # Last 4 characters
print("-" * 50)

# 5. Skipping characters using step
print("5. Skipping every other character with [::2]:")
print("credit_number[::2] =", credit_number[::2])

print("Skipping every 3rd character with [::3]:")
print("credit_number[::3] =", credit_number[::3])
print("-" * 50)

# 6. Masking (last 4 digits visible only)
print("6. Masking credit card number for privacy:")
last_digits = credit_number[-4:]
print(f"private: XXXX-XXXX-XXXX-{last_digits}")
print("-" * 50)

# 7. Reversing the string using step -1
print("7. Reversing the credit card number with [::-1]:")
reverse_credit_number = credit_number[::-1]
print(f"reversed: {reverse_credit_number}")
print("-" * 50)


# https://www.youtube.com/watch?v=7pXf1DUuaIo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=13