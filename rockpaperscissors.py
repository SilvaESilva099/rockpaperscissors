import random

player_options = ["rock", "paper", "scissors", "testicular torsion"]
options = ["rock", "paper", "scissors"]
options [0], [1], [2], [3]
computer_action = random.choice(options)
user_wins = 0
computer_wins = 0


while True:

    user_input = input("Choose an option: (Rock, Paper, Scissors, or press Q to quit:)\n").lower()
    if user_input == "q":
        break

    if user_input not in player_options:
        continue


    print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

    if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_input == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_input == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1
    elif user_input == "testicular torsion":
        print ("TESTICULAR TORSION! YOU WIN!")
        user_wins += 1

    keep_playing = input("Do you wish to play again? (yes or y/no or n)\n")
    if keep_playing != "yes":
        break

        
print ("You've won", user_wins, "times")
print ("The computer won", computer_wins, "times")
print ("See you next time!")