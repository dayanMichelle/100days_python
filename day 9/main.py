
import art
from os import system,name
print(art.logo)
people = []
def clear():
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")
def bid(person):
    people.append(person)

def winner(bid):
    high_score = 0
    winner = {}
    for person in bid:
        if person["price"] > high_score:
            high_score = person["price"]
            winner = person["name"]
    print(f"The winner is {winner} with a bid of ${high_score}")
    
continue_game = True
while continue_game:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid(
        {"name":name,
        "price":price}
        )
    is_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if is_continue == 'no':
        continue_game = False
    else:
        clear()

if continue_game == False:
    winner(people)


