# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#   doubles.append(x * 2)
doubles = [x * 2 for x in range(1, 11)]

# triples = []
# for y in range(1, 11)
#   trples.append(y * 3)  
triples = [y * 3 for y in range(1, 11)]

# squares = []
# for z in range(1, 11)
#   squares.append(z * z)
squares = [z * z for z in range(1, 11)]

print("doubles:", doubles)
print("triples:", triples)
print("squares:", squares)
print('-' * 60)
# ******************************************************* #
fruits = ["apple", "orange", "banana", "coconut"]

uppercase_words = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print("uppercase_words:", uppercase_words)
print("fruit_chars:", fruit_chars)
print('-' * 60)
# ******************************************************* #
numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

print("positive_numbers:", positive_numbers)
print("negative_numbers:", negative_numbers)
print("even_numbers:", even_numbers)
print("odd_numbers:", odd_numbers)
print('-' * 60)
# ******************************************************* #
grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print("passing_grades:", passing_grades)


# https://www.youtube.com/watch?v=YlY2g2xrl6Q&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=38