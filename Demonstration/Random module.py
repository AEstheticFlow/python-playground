# Random Module Full Demonstration 
# ----------------------------------------------
# Functions used:
# - randint(a, b)     → random integer between a and b (inclusive)
# - random()          → random float between 0 and 1
# - choice(seq)       → random element from a sequence
# - shuffle(seq)      → shuffle list in place
# - choices(seq, k=n) → pick n items with replacement (duplicates possible)
# - sample(seq, k=n)  → pick n unique items (no duplicates)

import random

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

print("-" * 60)
print("Available options:", options)
print("Original cards:", cards)
print("-" * 60)

# 1. randint()
print("1. Generating a random integer between 1 and 6:")
number_int = random.randint(1, 6)
print(f"random.randint(1, 6) → {number_int}")
print("-" * 60)

# 2. random()
print("2. Generating a random float between 0 and 1:")
number_float = random.random()
print(f"random.random() → {number_float}")
print("-" * 60)

# 3. choice()
print("3. Selecting a random option from tuple:")
chosen_option = random.choice(options)
print(f"random.choice(options) → {chosen_option}")
print("-" * 60)

# 4. shuffle()
print("4. Shuffling the deck of cards:")
random.shuffle(cards)
print(f"Shuffled cards: {cards}")
print("-" * 60)


# 5. choices()
print("5. Picking multiple items WITH replacement (duplicates possible):")
random_choices = random.choices(cards, k=5)
print(f"random.choices(cards, k=5) → {random_choices}")
print("-" * 60)

# 6. sample()
print("6. Picking multiple UNIQUE items (no duplicates):")
random_sample = random.sample(cards, k=5)
print(f"random.sample(cards, k=5) → {random_sample}")
print("-" * 60)


# https://www.youtube.com/watch?v=6uuuWox-uW0