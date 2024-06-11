from library import MENU, resources
drink_choice = ""
while drink_choice != "off":
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice in MENU:
        drink = MENU[drink_choice]
        if drink["ingredients"]["water"] > resources["water"]:
            print(f"Not enough water to make {drink_choice}")
        elif drink["ingredients"]["milk"] > resources["milk"]:
            print(f"Not enough milk to make {drink_choice}")
        elif drink["ingredients"]["coffee"] > resources["coffee"]:
            print(f"Not enough coffee to make {drink_choice}")
        else:
            resources["water"] -= drink["ingredients"]["water"]
            resources["milk"] -= drink["ingredients"]["milk"]
            resources["coffee"] -= drink["ingredients"]["coffee"]
            print(f"Here is your {drink_choice}")
    if drink_choice == "report":
        print(f"{resources}")
