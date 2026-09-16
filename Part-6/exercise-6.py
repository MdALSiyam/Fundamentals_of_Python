""" Practise Exercise-6
Gues the Lucky Number Game"""

import random

def play_game():
    lucky_number = random.randint(1, 50)

    while True:
        user_number = int(input("Guess the lucky number (1-50): "))
        if user_number == lucky_number:
            print("You won. Game Over!")
            break
        elif user_number < lucky_number:
            print("Too Low")
    else:
        print("Too High")
print("Thank you for playing the game")

play_game()

