# OOP Coffee Machine

from menu import Menu
from coffee_maker import CoffeeMaker
from money import Money
from logo import logo


def get_input(choices_list):
    while True:
        user_choice = input("> ").lower()
        if user_choice not in choices_list:
            formatted_choices = ""
            for i in range(len(choices_list)):
                if i == 0:
                    formatted_choices += f'"{choices_list[i]}"'
                elif i < len(choices_list) - 1:
                    formatted_choices += f', "{choices_list[i]}"'
                else:
                    formatted_choices += f' or "{choices_list[i]}"'
            print(f"Invalid choice. Please type {formatted_choices}.")
        else:
            return user_choice


machine_on = True
machine = CoffeeMaker()
money_machine = Money()
menu = Menu()
while machine_on:
    print(logo)
    print(f"Please choose a beverage: {menu.get_items()}")
    choice = get_input(["latte", "espresso", "cappuccino", "report", "off"])
    if choice == "report":
        machine.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        bev = menu.find_drink(choice)
        if machine.is_resource_sufficient(bev):
            print(f"Please insert ${bev.cost}.")
            if money_machine.make_payment(bev.cost):
                machine.make_coffee(bev)

print("Goodbye.")