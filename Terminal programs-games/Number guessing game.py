import random

print("*****************NUMBER GUESSING GAME*****************")
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0

print(f"Guess a number between {lowest_num} and {highest_num}")

while True:
    guess = input("Enter your guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if (guess > highest_num) or (guess < lowest_num):
            print(f"please guess a number only between {lowest_num} and {highest_num}")
            continue
        elif (guess > answer):
            highest_num = guess - 1
            print("***********************")
            print(f"Guess between {lowest_num} and {highest_num}")
        elif (guess < answer):
            lowest_num = guess + 1
            print("***********************")
            print(f"Guess between {lowest_num} and {highest_num}")
        else:
            print("***********************")
            print(f"Correct answer!!! You took {guesses} guesses")
            print('*' * 54)
            break
        
    else:
        print(f"please guess a number only between {lowest_num} and {highest_num}")
    

# https://www.youtube.com/watch?v=jcKe13D6bao