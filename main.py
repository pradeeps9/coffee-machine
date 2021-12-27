from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menuitem = MenuItem

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

machine_is_on = True

while machine_is_on:

    option = menu.get_items()
    choice = input(f"What would you link {option}")

    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)











