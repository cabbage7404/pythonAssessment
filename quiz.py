#sets the price for each fruit
fruits = {"Apple":"0.50",
          "Orange":"1.00",
          "Banana":"4.30",
          "Grape":"12.99",
          "Blueberry":"6.99"}

#sets the discount tiers to constants
options = {"50":"0.95",
           "100":"0.90",
           "150":"0.80",}

#sets the options to a constant
options_list = ["1. Add item", "2. Remove item", "3. Finish shopping", "4. Cancel"]


user_cart = {}

integer = 1

#sets the user's cart total to 0 
cart_total = 0
#sets the user's budget to 0
user_budget = 0

def search_cart(user_cart, item):
    if item in user_cart:
        return user_cart[item]
    return None

#while loop continue or end code
while True:
    #asks the user if they want to start
    start = input("Do you want to start the shopping cart program? Yes or No: ")
    if start == "yes" or start == "no":
        if start.lower() == "yes":
            break
        elif start.lower() == "no":
            print("You have exited the quiz")
            quit()
    else:
        print("Please enter Yes or No")

while True:
    user_name = input("Please enter your name: ") #asks users if they want to view the rules
    if user_name.isalpha(): #prints the rules if player wants to view them
        print("")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("")
        print(f"Welcome {user_name.capitalize()}!")
        print("")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("")
        break
    else:
        print("Please enter your name in alphabetical format")

#prints the lines of options
for options in options_list:
    print(f"{options}")

#while loop to ask user what they want to do
while True:
    try:
        #asks the user what they want to do
        print("")
        print("Please enter what you want to do next with the corresponding number")
        user_option = input("Enter number: ")
        
        if user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4":
            if user_option == "1":
                print("Here are the options for Fruits: ")
                for fruit, price in fruits.items():
                    print(f"{fruit} : ${price}")
                fruit_choice = input("Please enter which fruit you would like (Apple, Orange, Banana, Grape, Blueberry): ")
                if fruit_choice.upper() == "APPLE" or fruit_choice.upper() == "ORANGE" or fruit_choice.upper() == "BANANA" or fruit_choice.upper() == "GRAPE" or fruit_choice.upper() == "BLUEBERRY":
                    if fruit_choice.upper() == "APPLE":
                        fruit_choice_amount = input("How many would you like: ")
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Apple"]
                            fruit_price = float(fruit_price)
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item)
                            if user_item_amount is not None:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
                            else:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "ORANGE":
                        fruit_choice_amount = input("How many would you like: ")
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Orange"]
                            fruit_price = float(fruit_price)
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item)
                            if user_item_amount is not None:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
                            else:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "BANANA":
                        fruit_choice_amount = input("How many would you like: ")
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Banana"]
                            fruit_price = float(fruit_price)
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item)
                            if user_item_amount is not None:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
                            else:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "GRAPE":
                        fruit_choice_amount = input("How many would you like: ")
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Grape"]
                            fruit_price = float(fruit_price)
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item)
                            if user_item_amount is not None:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
                            else:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "BLUEBERRY":
                        fruit_choice_amount = input("How many would you like: ")
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Blueberry"]
                            fruit_price = float(fruit_price)
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item)
                            if user_item_amount is not None:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
                            else:
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount
                        else:
                            print("Please enter your input in digits")
                else:
                    print("Please enter your answer again.")
            elif user_option == "2":
                if len(user_cart) == 0:
                    print("You have nothing in your cart.")
                else:
                    for fruit, amount in user_cart.items():
                        print(f"{fruit} : {amount}")
                    user_item_remove = input("Which item do you want to remove: ")
                    if user_item_remove.capitalize() in user_cart:
                        user_item_remove_amount = input("How many would you like to remove: ")
                        if user_item_remove_amount.isdigit():
                            user_item_remove_amount = int(user_item_remove_amount)
                            if user_item_remove_amount > user_cart[user_item_remove.capitalize()]:
                                print("You don't have that many items in your cart.")
                            else:
                                user_cart[user_item_remove.capitalize()] = user_cart[user_item_remove.capitalize()] - user_item_remove_amount
                                print(user_item_remove_amount)
                                print(user_cart)
                                fruit_price = float(fruits[user_item_remove.capitalize()])
                                user_item_remove_amount = int(user_item_remove_amount)
                                item_total = user_item_remove_amount * fruit_price
                                cart_total = cart_total - item_total
                                print(cart_total)
                        else:
                            print("Please enter amount in digits.")
                    else:
                        print("You don't have that item in your cart.")
            elif user_option == "3":
                print(f"Your total is ${cart_total}")
                exit()
            elif user_option == "4":
                print("You have exited the program.")
                quit()
        else:
            print("Please enter your choice in digits: ")
    except ValueError:
        print("An error has occured.") #prints if error occurs

