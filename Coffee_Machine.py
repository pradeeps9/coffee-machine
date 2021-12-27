MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0
}

# toc = types of coins
toc = {
    "quarters": 25,
    "dimes": 10,
    "nickles": 5,
    "penny": 1
}


def process_transaction(qu, di, ni, pe, ordered_coffee):
    total_money = (qu*toc["quarters"] + di*toc["dimes"] + ni*toc["nickles"] + pe*toc["penny"])/100
    orderamt = MENU[ordered_coffee]["cost"]
    change = total_money - orderamt
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return
    elif change >= 0:
        print(f"Here is ${change} in change")
        make_coffee(ordered_coffee)
        resources["money"] += orderamt


def make_coffee(order):

    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

    print(f"Here is your {order} ☕. Enjoy!")


def ingredients_finished(ordr):
    if resources['water'] < MENU[ordr]['ingredients']['water']:
        return True
    elif resources['coffee'] < MENU[ordr]['ingredients']['coffee']:
        return True
    elif resources['milk'] < MENU[ordr]['ingredients']['milk']:
        return True
    else:
        return False


coffee_machine_is_on = True
while coffee_machine_is_on:

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        coffee_machine_is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${resources['money']}")

    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        if ingredients_finished(order):
            print("Sorry there is not enough ingredients.")
            continue
        print("Please insert coins.")
        q = int(input("how many quarters?: "))
        d = int(input("how many dimes?: "))
        n = int(input("how many nickles?: "))
        p = int(input("how many pennies?: "))

        process_transaction(q, d, n, p, order)

