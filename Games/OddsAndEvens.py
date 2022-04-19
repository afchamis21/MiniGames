import random
import sys


def play():
    options = ["odd", "even"]
    user_score = 0
    computer_score = 0
    winner = ""

    while True:
        print(f"user: {user_score} | computer: {computer_score}")
        user_mode = input("Choose Odd, Even or E to exit the program: ").lower()

        if user_mode == "e":
            sys.exit("See you next time!")

        if user_mode not in options:
            print("Invalid Choice!\n")
            continue

        user_pick = input("Now choose a number from 0 to 10: ")

        try:
            user_pick = int(user_pick)
        except ValueError:
            print("Invalid Number!\n")
            continue

        if user_pick > 10 or user_pick < 0:
            print("Invalid Number!\n")
            continue

        computer_pick = random.randint(0, 10)

        result = (user_pick + computer_pick) % 2

        if user_mode == "odd":
            if result == 1:
                user_score += 1
                winner = "User"
            else:
                computer_score += 1
                winner = "Computer"
        else:
            if result == 0:
                user_score += 1
                winner = "User"
            else:
                computer_score += 1
                winner = "Computer"

        print(f"Computer chose {computer_pick}!")
        print(f"{winner} Wins\n")
