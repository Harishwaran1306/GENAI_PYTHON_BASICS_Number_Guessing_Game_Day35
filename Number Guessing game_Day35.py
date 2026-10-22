#Number Guessing Game:

import random


Hidden_Number = random.randint(1,50)

Attempts = 0

while True:
    Guess = int (input('Enter the Number Between 1 - 50:'))
    Attempts = Attempts + 1

    if Guess == Hidden_Number:
        print(f"Correct!!! You guessed in {Attempts} attempts")
        break
    elif Guess < Hidden_Number:
        print("Too Low! Try bigger number")
    else:
        print("Too High! Try smaller number")

    if Attempts == 5:
        print(f" Lost the Game!!! The Hidden_Number is {Hidden_Number} ")
        break
