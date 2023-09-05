running = True
profit = 0

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
def check_money():
    """return the total amount of money cust inserted in"""
    print(f"Please insert coins ! Your order ${drink['cost']}")
    total = float(input("How many quaters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total

def successful_transaction(money_received, cost):
    """check whether the money sufficient to make purchase """
    if money_received == cost:
        print("Your order had been paid")
    elif money_received > cost:
        changed = round(money_received - cost,2)
        print(f"Here's your changed ${changed}")
        global profit
        profit += cost
        return True
    else:
        print("You are not insert enough money to make this purchase ! Money refunded.")
        return False

def check_resources(order_ingredients):
    """to check whether the resources are sufficient to make the coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough ingredients to make your {ask_for_order} =((")
            return False
    return True

def coffee(drink_name,order_ingredients):
    """deduct the ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here you are. Enjoy your {drink_name}")

while running:
    # def order(menu, resources):
    ask_for_order = input("What would you like (latte / espresso / cappuccino) :  ").lower()
    if ask_for_order == "report":
        print(resources)
        print(f"Our current profit is {profit}")
    elif ask_for_order == "off":
        running = False
    else:
        drink = menu[ask_for_order]
        if check_resources(drink["ingredients"]):
            payment = check_money()
            if successful_transaction(payment, drink["cost"]):
                coffee(ask_for_order,drink["ingredients"])
