from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
global profit

def run_machine():
    """Runs the coffee machine. Based on given classes.
    Maintenance Engineer can turn off the machine using an Off command or request a report."""
    try:
        my_menu = Menu()
        my_coffee_maker = CoffeeMaker()
        my_money_machine = MoneyMachine()
        options = my_menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()
        if choice == "off":
             print("Shutting down!")
             return
        elif choice == "report":
             my_coffee_maker.report()
             my_money_machine.report()
        else:
            chosen = my_menu.find_drink(choice)
            if chosen and my_coffee_maker.is_resource_sufficient(chosen):
                payment_successful = my_money_machine.make_payment(chosen.cost)
                if payment_successful:
                    my_coffee_maker.make_coffee(chosen)
            run_machine()

    except(AttributeError, ValueError):
        print("Please try again.")
        run_machine()

run_machine()
