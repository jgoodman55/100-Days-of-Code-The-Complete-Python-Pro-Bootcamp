from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_status = 'on'
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while machine_status == 'on':
    valid_input = False
    while not valid_input:
        options = menu.get_items()
        user_input = input(f'What would you like? {options}: ').lower()
        if user_input not in ["espresso", "latte", "cappuccino", "off", "report"]:
            print("Please enter a valid input. (espresso/latte/cappuccino/off/report)")
        else:
            valid_input = True
            if user_input == 'off':
                machine_status = 'off'
            elif user_input == 'report':
                coffee_maker.report()
                money_machine.report()
            else:
                drink = menu.find_drink(user_input)
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
