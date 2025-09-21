import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

# Dictionary of int : tuple
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}
# ----------------------------------------------------- #

def display_man(wrong_guesses):
    print('*' * 10)
    for line in hangman_art[wrong_guesses]:
        print(f"{line:^10}")
    print('*' * 10)
# ----------------------------------------------------- #

def display_hint(hint):
    print(" ".join(hint))
# ----------------------------------------------------- #

def display_answer(answer):
    print(" ".join(answer))  
# ----------------------------------------------------- #

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    
    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!!")
            print('*' * 10)
            continue

        if guess in guessed_letters:
            print("You guessed this letter before!!")
            continue
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        
        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You won!!!") 
            break

        if wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost!!") 
            break
# ************************************************************** #
        
if __name__ == '__main__':
    main()


# https://www.youtube.com/watch?v=ag8NtD1e0Kc&t=120s