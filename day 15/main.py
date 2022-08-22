from os import system, name
from art import LOGO


def clear():
    '''
    Fuction to clear the console
    '''
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


print(LOGO)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins_total = 0


def adding_coins(quarters_user, dimes_user, nickles_user, pennies_user, drink):
    sum_coins = 0.25 * quarters_user + 0.10 * dimes_user + 0.05 * nickles_user + 0.01 * pennies_user
    if drink["cost"] > sum_coins:
        return 1
    elif drink["cost"] < sum_coins:
        rest = sum_coins - drink["cost"]
        print(f"Here is {round(rest, 1)} in change.")
    total_sum = sum_coins - rest
    return total_sum


def make_coffee(drink_user):
    resources["water"] -= drink_user["water"]
    resources["coffee"] -= drink_user["coffee"]
    if len(drink_user) == 3:
        resources["milk"] -= drink_user["milk"]
    print(f"Here is your {drink_selected} ☕️. Enjoy!")


need_drink = True

while need_drink:

    drink_selected = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_selected == "off":
        need_drink = False
        clear()
        break

    if drink_selected == "report":
        clear()
        print(LOGO)
        for k, v in resources.items():
            print(f"{k}: {v}")
        print(f"Money: ${coins_total}")

    else:

        for k, v in MENU.items():
            if drink_selected == k:
                drink = v

        drink_ingredients = drink["ingredients"]

        if drink_ingredients["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif drink_ingredients["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        elif len(drink_ingredients) == 3 and drink_ingredients["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        else:
            print("Please insert coins.")
            quarters = float(input("how many quarters?: $"))
            dimes = float(input("how many dimes?: $"))
            nickles = float(input("how many nickles?: $"))
            pennies = float(input("how many pennies?: $"))
            coins = adding_coins(quarters, dimes, nickles, pennies, drink)
            if coins == 1:
                print("Sorry that's not enough money. Money refunded.")
            else:
                coins_total += coins
                make_coffee(drink_ingredients)
