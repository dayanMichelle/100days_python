from art import logo,win,lose
import random

print(logo)
def play_game():
  '''
  Start the game
  '''
  number = random.randint(0,100)
  lives = 0
  print("I'm thinking of a number between 1 and 100.")
  print(f"Pssst, the correct answer is {number}")
  continue_game = True
  dificult = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if dificult == 'easy':
    lives = 10
  elif dificult == 'hard':
    lives = 5
  else:
    return print("It's no a option.")

  while continue_game:
    guess = int(input("Make a guess:"))
    if guess != number:
      lives -=1
      if guess > number:
        print('''
        Too hight.
        ''')
      else:
        print('''
        Too low.
        ''')
      if lives == 0:
        return print(lose)
      else:
        print(f'''
        Guess again.
        You have {lives} attempts remaining to guess the number.
        ''')
    else:
      return print(win)
  

play_game()