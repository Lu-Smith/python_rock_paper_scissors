import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randindt(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_guess = options[random_number]
    print("Computer picked, " + computer_guess + ".")


print("Goodbye")

