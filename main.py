# Coffee machine example
# Alexandru Meta
# 2/22/23

import coffee_maker
import menu
import money_machine

money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

