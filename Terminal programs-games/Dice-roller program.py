# ● ┌ ─ ┐ │ └ ┘

import random

dice_art = {                # A dictionary of keys = integers & values = tuples
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))       # dice = [r_n1, r_n2, r_n3,...]
print(dice)

# PRINT VERTICALLY
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)


# PRINT HORIZONTALLY
for line in range(5):       # 5 = number of lines, size of every tuple
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total += die
print(f"total: {total}")


# https://www.youtube.com/watch?v=x-Ag2_bJ40Y