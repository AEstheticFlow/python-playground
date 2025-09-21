def showBalance(money):
    print(f"Your balance is: ${money:.2f}")
# --------------------------------------------------- #

def deposit():
    amount = input("Enter an amount to deposit: ")
    if amount.isalpha():
        print("Insufficint fund!!")
        return 0
    else:
        amount = float(amount)
        if amount <= 0:
            print("Insufficint fund!!")
            return 0
        else:
            return amount   
# --------------------------------------------------- #

def withDraw(money):
    amount = input("Enter an amount to withdraw: ")
    if amount.isalpha():
        print("Insufficint fund!!")
        return 0
    else:
        amount = float(amount)
        if (amount <= 0) or (amount > money):
            print("Insufficint fund!!")
            return 0
        else:
            return amount
# **************************************************** #

def main():
    print("***************BANKING PROGRAM***************\n")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print('*' * 45)

    balance = 150.00
    
    while True:
        choice = input("Choose between (1 → 4): ")
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 1:
                    showBalance(balance)
                    print('*' * 45)
                case 2:
                    balance += deposit()
                    print('*' * 45)
                case 3:
                    balance -= withDraw(balance)
                    print('*' * 45)
                case 4:
                    print("\n**********Thank you. Have a good day**********")
                    break
                case _:
                    print("Invalid choice!!")
                    print('*' * 45)
        else:
            print("Invalid choice!!")
            print('*' * 45)
# **************************************************** #

if __name__ == '__main__':
    main()


# https://www.youtube.com/watch?v=8aW3tkIul-8