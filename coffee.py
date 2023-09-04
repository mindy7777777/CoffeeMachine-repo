running = True

while running:
    menu = {
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

    resources = {"water": 300,
                 "milk": 200,
                 "coffee": 100
                 }

    # def order(menu, resources):
    ask_for_order = input("What would you like (latte / espresso / cappuccino) :  ").lower()
    if ask_for_order in menu:
        drink = menu[ask_for_order]
        if all(resources[ingredients] >= amount for ingredients, amount in drink["ingredients"].items()):
            resources["ingredients"] -= amount
            print(f"Here's your {ask_for_order}. Enjoy !")
        else:
            print(f"Sorry, not enough ingredients to make your {ask_for_order} =((")
    elif ask_for_order == "report":
        print(resources)
    elif ask_for_order == "off":
        running = False
