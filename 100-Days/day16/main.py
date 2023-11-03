from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import sys

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        option = input(f"What would you like to drink? ({menu.get_items()}) ")
        if option == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        if option == "off":
            sys.exit()
        
        drink = menu.find_drink(option)
        if drink == None or not coffee_maker.is_resource_sufficient(drink):
            continue

        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()