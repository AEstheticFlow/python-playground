menu = {"pizza": 3.5,
        "popcorn": 5,
        "fries": 2,
        "soda": 4.5,
        "hotdog": 2.5,
        "nacho": 6}

cart = []
total = 0

print("**************MENU**************")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("********************************")

while True:
    food = input("Choose from the menu ('q' to quit): ")
    if food.lower() == "q":
        break
    # print(menu.get('Something not in dictionary')) == None
    elif menu.get(food) is None:
        print("We don't have that!")
    else:
        cart.append(food)
        total += menu.get(food)     # Adds the values of the keys

print("**************CART**************")
for thing in cart:
    print(thing, end = " ")
print("\n********************************")

print(f"Your total is: {total:.2f}")


# https://www.youtube.com/watch?v=PbkIzW_70EI