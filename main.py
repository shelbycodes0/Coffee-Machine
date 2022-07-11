from coffeedata import menu, resources
is_on = True
profit = 0


def is_resources_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, there is not enough {item} to make your order. Try again later.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Please take your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}! ☕")


def process_coins():
    print("Please insert coins.")
    total = int(input("Number of quarters: ")) * .25
    total += int(input("Number of quarters: ")) * .10
    total += int(input("Number of quarters: ")) * .05
    total += int(input("Number of quarters: ")) * .01
    return total


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resources_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])


