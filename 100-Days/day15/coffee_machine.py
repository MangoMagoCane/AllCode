import sys
from data import *

profits = 0

def main():
    while True:
        drink = get_drink(MENU)

        if drink == "report":
            print_report()
            continue

        if not resource_check(drink):
            continue
       
        for rsc in MENU[drink]["ingredients"]:
            resources[rsc] -= MENU[drink]["ingredients"][rsc]
        
        money_inserted = transaction(MONEY)
        drink_cost = MENU[drink]["cost"]
        if money_inserted > drink_cost:
            print(f'Here is ${money_inserted - drink_cost:.2f} in change.')
        elif money_inserted < drink_cost:
            print("Sorry, not enough money. Money refunded.")
            continue
            
        print(f"Here is your {drink}. Enjoy!")
        global profits
        profits += drink_cost


def transaction(money):
    money_inserted = 0
    print("Please insert coins.")

    for coin in money:
        while True:
            try:
                coin_amount = int(input(f"How many {coin}? "))
                if coin_amount >= 0:
                    money_inserted += money[coin] * coin_amount
                    break
            except Exception as e:
                pass
            print("Unrecognized input.")

    return round(money_inserted, 2)


def resource_check(drink):
    ingredients = MENU[drink]["ingredients"]
    missing_ingredients = []
    resources_available = True

    for ingred in ingredients:
        if resources[ingred] < ingredients[ingred]:
            resources_available = False
            missing_ingredients.append(ingred)

    if missing_ingredients:
        print(f"Sorry, there is not enough {', '.join(missing_ingredients)}")

    return resources_available
    

def get_drink(menu):
    drinks = list(menu)
    while True:
        selected_drink = input(f"What would you like? ({'/'.join(drinks)}): ")

        if selected_drink in drinks:
            return selected_drink
        elif selected_drink == "report":
            return "report"
        elif selected_drink == "off":
            sys.exit()
        else:
            print("Not a valid drink type.")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profits}")


if __name__ == "__main__":
    main()