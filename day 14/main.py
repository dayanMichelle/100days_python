import random
import art
from game_data import data
from os import system,name

def clear():
    '''
    Fuction to clear the console
    '''
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")

def format_data(account):
    '''
    Format the account data into printable format
    '''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f'''
    {account_name}, a {account_descr}, from {account_country}
    '''


def correct_answer(accountA, accountB, answer):
    '''
    Params: ComaparationA y B 
            Answer
    Return: If answer is True or False 
    '''
    countA = accountA["follower_count"]
    countB = accountB["follower_count"]
    if countA > countB:
        return answer == "A"
    else:
        return answer == "B" 

print(art.logo)
accountB = random.choice(data)
continue_game = True

score = 0
while continue_game:
    accountA = accountB
    accountB = random.choice(data)
    while accountA == accountB:
        accountB  = random.choice(data)
    print(f"Compare A: {format_data(accountA)}")
    print(art.vs)
    print(f"Against B: {format_data(accountB)}")
  
    answer = input("Who has more followers? Type 'A' or 'B': ")
    result_of_answer = correct_answer(accountA, accountB,answer)
    clear()
    print(art.logo)
    if result_of_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")




    
