import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Testicular_Torsion = 3

class Actionputer(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Actionputer) - 1)
    actionputer = Actionputer(selection)
    return actionputer


user_wins = 0
computer_wins = 0
ties = 0

def determine_winner(user_action, computer_action):
    global user_wins, computer_wins, ties
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
        ties += 1
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1
    elif user_action == Action.Testicular_Torsion:
        if computer_action != Action.Testicular_Torsion:
            print("TESTICULAAAR TORSION! You win!")
            user_wins += 1
        else:
            print("MUTUAL DESTRUCTION! NOBODY WINS!")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    
print ("You've won", user_wins, "times")
print ("The computer won", computer_wins, "times")
print ("You've tied", ties, "times")
print ("See you next time!")