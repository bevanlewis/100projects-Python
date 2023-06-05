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

money = 0


# docstrings could also be added to make functions more informative.

def print_report():
    print(f'Water: {resources["water"]}ml\n'
          f'Milk: {resources["milk"]}ml\n'
          f'Coffee: {resources["coffee"]}g\n'
          f'Money: ${money}\n')


def check_resources(coffee_type):
    # This could have been solved by passing in the dictionary of required ingredients and then
    # looping through the dictionary.

    if resources['water'] > MENU[coffee_type]['ingredients']['water']:
        if resources['coffee'] > MENU[coffee_type]['ingredients']['coffee']:
            if coffee_type == 'espresso' or resources['milk'] > MENU[coffee_type]['ingredients']['milk']:
                return True, ''
            return False, 'milk'
        return False, 'coffee'
    else:
        return False, 'water'


def check_payment(money_paid, coffee_type):
    if money_paid >= MENU[coffee_type]['cost']:
        return True, round(money_paid - MENU[coffee_type]['cost'], 2)
    else:
        return False, round(money_paid, 2)


def make_coffee(coffee_type):
    # Dictionary looping can also be used here

    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    if coffee_type != 'espresso':
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']


# Main code

running = True

while running:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == 'off':
        print("Turning Off")
        running = False
    elif coffee_type == 'report':
        print_report()
    elif coffee_type in MENU.keys():
        valid_resources, missing = check_resources(coffee_type)
        if not valid_resources:
            print(f"Sorry there is not enough of {missing}")
            continue

        # This could be its own function
        quarters = int(input("Enter number of quarters ")) * 0.25
        dimes = int(input("Enter number of dimes ")) * 0.1
        nickles = int(input("Enter number of nickles ")) * 0.05
        pennies = int(input("Enter number of pennies ")) * 0.01

        total_money = quarters + dimes + nickles + pennies

        valid_payment, change = check_payment(total_money, coffee_type)

        if valid_payment and change != 0:
            print(f"Here is ${change} dollars in change")
            money += MENU[coffee_type]['cost']
        elif not valid_payment:
            print(f"Sorry not enough money returning {change}")
            continue
        else:
            money += MENU[coffee_type]['cost']

        make_coffee(coffee_type)
        print(f"Here is your {coffee_type} ☕️, Enjoy!")
    else:
        print("Not a valid command")
