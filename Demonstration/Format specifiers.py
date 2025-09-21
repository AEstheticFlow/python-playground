# Number Formatting Demonstration

number = 1234.56789
negative_number = -1234.56789
small_number = 0.045
big_number = 1000000

print("-" * 60)
print(f"Original number: {number}")
print(f"Negative number: {negative_number}")
print(f"Small number: {small_number}")
print(f"Big number: {big_number}")
print("-" * 60)

# 1. .(number)f = round to that many decimal places
print("1. Rounding to 2 decimal places using .2f:")
print(f"{number:.2f}")         # 1234.57
print("-" * 60)

# 2. :(number) = allocate that many spaces (right for floats/ints, left for strings)
print("2. Allocating 20 spaces:")
print(f"{number:20}")          
print("-" * 60)

# 3. :>(number) = right justify (overrides the default)
print("3. Right justified in 20 spaces:")
print(f"{number:>20}")         # Right-aligned
print("-" * 60)

# 4. :<(number) = left justify  (overrides the default)
print("4. Left justified in 20 spaces:")
print(f"{number:<20}")         # Left-aligned
print("-" * 60)

# 5. :0(number) = zero pad in that many spaces
print("5. Zero-padded in 10 spaces:")
print(f"{int(number):010}")    # Pads with zeros: 000012345
print("-" * 60)

# 6. :^(number) = center align
print("6. Center aligned in 10 spaces:")
print(f"{number:^10}")         # Centered
print("-" * 60)

# 7. :+ = include sign for positive and negative
print("7. Show + for positive numbers:")
print(f"{number:+}")           # +1234.56789
print(f"{negative_number:+}")  # -1234.56789
print("-" * 60)

# 8. := = sign goes to leftmost position (for padding)
print("8. Sign to leftmost position with zero padding:")
print(f"{negative_number:=+10}")  # -0001234.56789 (sign leftmost)
print("-" * 60)

# 9. : (space) = insert a space before positive numbers
print("9. Space before positive, nothing added for negative:")
print(f"{number: }")              #  1234.56789
print(f"{negative_number: }")     # -1234.56789
print("-" * 60)

# 10. :, = comma as thousand separator
print("10. Comma as thousand separator:")
print(f"{big_number:,}")          # 1,000,000
print("-" * 60)

# 11. :% = percentage format
print("11. Percentage format (multiplies by 100 and adds %):")
print(f"{small_number:%}")        # 4.500000%
print(f"{small_number:.2%}")      # 4.50%
print("-" * 60)


# https://www.youtube.com/watch?v=FrvBwdAU2dQ