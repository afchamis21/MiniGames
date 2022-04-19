import random
import sys


def play():
    options = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0
    winner = ""

    while True:
        print(f"user: {user_score} | computer: {computer_score}")

        user_pick = input("Choose Rock, Paper, scissors or E to exit the program: ").lower()

        computer_pick = options[random.randint(0, 2)]

        if user_pick == computer_pick:
            print("It's a tie!\n")
            continue

        match user_pick:
            case "e":
                sys.exit("See you next time!")
            case "rock":
                if computer_pick == "paper":
                    computer_score += 1
                    winner = "Computer"
                else:
                    user_score += 1
                    winner = "User"

            case "paper":
                if computer_pick == "scissors":
                    computer_score += 1
                    winner = "Computer"
                else:
                    user_score += 1
                    winner = "User"

            case "scissors":
                if computer_pick == "rock":
                    computer_score += 1
                    winner = "Computer"
                else:
                    user_score += 1
                    winner = "User"

            case _:
                print("Invalid input! Please choose Rock, Paper or scissors\n")
                continue

        print(f"Computer chose: {computer_pick}!")
        print(f"{winner} Wins!\n")
