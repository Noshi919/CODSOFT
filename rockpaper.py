import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_images = [rock, paper, scissors]

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))


if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, you lose.")
else:
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    
    if computer_choice == user_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:  # Rock crushes Scissors
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:  # Scissors is crushed by Rock
        print("You lose.")
    elif computer_choice > user_choice:  # Paper covers Rock, Scissors cuts Paper
        print("You lose.")
    elif user_choice > computer_choice:  # Rock is covered by Paper, Paper is cut by Scissors
        print("You win!")
