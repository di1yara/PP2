"""
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:

"""
import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    while True:
        try:
            guess = int(input("Take a guess: "))
    
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("You find the secret number!!!")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

guess_the_number()
