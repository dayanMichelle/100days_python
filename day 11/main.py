# pylint: disable=unused-variable
############### Blackjack Project #####################
''''
Definición de las reglas del juego
'''
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
from os import system,name
import random
import art

def clear():
    '''
    Clea the console
    '''
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")


def count(list_sum):
    '''
    Suma las cartas
    '''
    counter = 0
    for index, i in enumerate(list_sum, 0):
        counter += list_sum[index]
        if 11 in list_sum and counter > 21:
            list_sum[index] = 1
    return counter


def winner(computer_player,user_player):
    '''
    Define el aganador del juego
    retorna un string indicando si ganaste o perdiste
    '''
    user_counter = count(user_player)
    computer_counter = count(computer_player)

    if user_counter == computer_counter:
        return print(f'''
            Play computer: {computer_player} 
            Your play: {user_player}
            A Draw
            ''')
    elif 21 > user_counter > computer_counter:
        return print(f'''
            Play computer: {computer_player} 
            Your play: {user_player}
            You Win
            ''')

    elif 21 > computer_counter > user_counter:
        return print(f'''
            Play computer: {computer_player} 
            Your play: {user_player}
            You Lose
            ''')
    elif user_counter > 21:
        return print(f'''
            Play computer: {computer_player} 
            Your play: {user_player}
            You Lose
            ''')
    elif computer_counter > 21:
        return print(f'''
            Play computer: {computer_player} 
            Your play: {user_player}
            You Win
            ''')
    return "I know what happend"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    '''
    Play the game
    '''
    print(art.logo)
    computer_player = [random.choice(cards), random.choice(cards)]
    user_player = [random.choice(cards),random.choice(cards)]
    print(computer_player[0], '*')
    print(user_player)

    count_user = count(user_player)
    if count_user == 21:
        winner(computer_player,user_player)
    elif count(computer_player) == 21:
        winner(computer_player,user_player)
    else:
        is_hit = True
        while is_hit and count_user <= 21:
            want_hit = input("Quiere elegir otra carta 'hit' o pasar 'stand': ")
            if want_hit == "hit":
                add_value = random.choice(cards)
                user_player.append(add_value)
                print(user_player)
                count_user = count(user_player)
                if count_user >= 21:
                    winner(computer_player,user_player)
            else:
                is_hit = False
                winner(computer_player,user_player)
            
            

play_game()

while input("¿Do you want to play a game of Blackjack? Type 'y' or 'n' ") == 'y':
    clear()
    play_game()
