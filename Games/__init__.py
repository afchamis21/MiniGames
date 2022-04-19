import sys

from Games import RockPaperScissor, OddsAndEvens


def start():
    selection = input("Choose Rock Paper Scissors [1] or Odds and Evens [2] or E to exit the program: ").lower()

    if not selection.isdigit():
        print("Invalid Selection! Choose 1, 2 or E\n")
        return start()

    match selection:
        case "1":
            RockPaperScissor.play()
        case "2":
            OddsAndEvens.play()
        case "e":
            sys.exit("See you next time!")
        case _:
            print("Invalid Selection! Choose 1, 2 or E\n")
            return start()
