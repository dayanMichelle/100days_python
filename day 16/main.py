from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
is_on = True
menu = Menu()
money = MoneyMachine()
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        make_coffee.report()
        money.report()
    elif choice == "off":
        is_on = False
    else:
        order = menu.find_drink(choice)
        if order and make_coffee.is_resource_sufficient(order) and money.make_payment(order.cost):
            make_coffee.make_coffee(order)
