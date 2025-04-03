import random

choices = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You Win!")
else:
    print("You Lose!")
