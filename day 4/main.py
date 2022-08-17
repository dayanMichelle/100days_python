# pylint: disable=missing-module-docstring
import random
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [ROCK,PAPER, SCISSORS]
user_choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n "))

computer_choice = random.randint(0,2)

if user_choice >=3 or user_choice<0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You wins")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == 0 and user_choice==2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
