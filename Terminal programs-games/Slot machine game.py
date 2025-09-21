# Python Slot Machine
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    # List comprehension, returns a list:
    return [random.choice(symbols) for symbol in range(3)] 

    # Longer method:

    # results = []
    # for symbol in range(3):
    #    results.append(random.choice(symbols))
    # return results
# ----------------------------------------------------- #

def print_row(row):
    print('*' * 15)
    print(" | ".join(row))
    print('*' * 15)
# ----------------------------------------------------- #

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0
# ******************************************************************* #

def main():
    balance = 100

    print('*' * 25)
    print(" Welcome to Python Slots ")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print('*' * 25)

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount:$ ")

        if not bet.isdigit():
            print("Please enter a valid number!!")
            print('*' * 25)
            continue

        bet = int(bet)      # Excecuted directly if the previous isn't True

        if bet > balance:
            print("Insufficient funds!!")
            print('*' * 25)
            continue 
        if bet <= 0:
            print("Bet must be greater than 0!!")
            print('*' * 25)
            continue

        balance -= bet      # Excecuted directly if the previous isn't True

        row = spin_row()    # Variable that contains a list of three emojis
        print("Spinning...⏱️")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
            balance += payout
        else:
            print("Sorry you lost this round😔")

        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    print('*' * 45)
    print(f"Game over! Your final balance is ${balance}")
    print('*' * 45)
# ******************************************************************* #

if __name__ == '__main__':
    main()


# https://www.youtube.com/watch?v=f5J3YiZ3XX8&t=5s