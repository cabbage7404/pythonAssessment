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

#sets user cart to an empty dictionary to be used
user_cart = {}

#sets the user's cart total to 0 
cart_total = 0
#sets the user's budget to 0
user_budget = 0

#function to search user's cart for an item
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
        print("")
        print("Please enter what you want to do next with the corresponding number") #asks the user what they want to do
        user_option = input("Enter number: ")
        if user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4": #checks if the user input is one of the 4 options
            if user_option == "1":
                print("Here are the options for Fruits: ")
                for fruit, price in fruits.items():
                    print(f"{fruit} : ${price}")
                fruit_choice = input("Please enter which fruit you would like (Apple, Orange, Banana, Grape, Blueberry): ") #asks which fruit the user wants to add
                if fruit_choice.upper() == "APPLE" or fruit_choice.upper() == "ORANGE" or fruit_choice.upper() == "BANANA" or fruit_choice.upper() == "GRAPE" or fruit_choice.upper() == "BLUEBERRY":
                    if fruit_choice.upper() == "APPLE": #continues if the user enters "Apple"
                        fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                        if fruit_choice_amount.isdigit(): 
                            fruit_price = fruits["Apple"] #takes the price of the item
                            fruit_price = float(fruit_price) #converts price to float
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price #calculates total item price of all added items
                            cart_total = cart_total + item_total #adds item price to user total
                            print(f"Your total is now ${cart_total}.") #prints user total
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has that item in their cart
                            if user_item_amount is not None: #if user already has the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
                            else: #if user doesn't have the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "ORANGE": #continues if the user enters "Orange"
                        fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                        if fruit_choice_amount.isdigit(): 
                            fruit_price = fruits["Orange"] #takes the price of the item
                            fruit_price = float(fruit_price) #converts price to float
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price #calculates total item price of all added items
                            cart_total = cart_total + item_total #adds item price to user total
                            print(f"Your total is now ${cart_total}.") #prints user total
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has that item in their cart
                            if user_item_amount is not None: #if user already has the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
                            else: #if user doesn't have the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "BANANA": #continues if the user enters "Banana"
                        fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Banana"] #takes the price of the item
                            fruit_price = float(fruit_price) #converts price to float
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price
                            cart_total = cart_total + item_total
                            print(f"Your total is now ${cart_total}.")
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has that item in their cart
                            if user_item_amount is not None: #if user already has the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
                            else: #if user doesn't have the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "GRAPE": #continues if the user enters "Grape"
                        fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Grape"] #takes the price of the item
                            fruit_price = float(fruit_price) #converts price to float
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price #calculates total item price of all added items
                            cart_total = cart_total + item_total #adds item price to user total
                            print(f"Your total is now ${cart_total}.") #prints user total
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has that item in their cart
                            if user_item_amount is not None: #if user already has the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
                            else: #if user doesn't have the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart
                        else:
                            print("Please enter your input in digits")
                    elif fruit_choice.upper() == "BLUEBERRY": #continues if the user enters "Blueberry"
                        fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                        if fruit_choice_amount.isdigit():
                            fruit_price = fruits["Blueberry"] #takes the price of the item
                            fruit_price = float(fruit_price) #converts price to float
                            fruit_choice_amount = int(fruit_choice_amount)
                            item_total = fruit_choice_amount * fruit_price #calculates total item price of all added items
                            cart_total = cart_total + item_total #adds item price to user total
                            print(f"Your total is now ${cart_total}.") #prints user total
                            item = "Apple"
                            user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has that item in their cart
                            if user_item_amount is not None: #if user already has the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
                            else: #if user doesn't have the item
                                user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart
                        else:
                            print("Please enter your input in digits")
                else:
                    print("Please enter your answer again.")
            elif user_option == "2": #checks if the user's cart is empty
                if len(user_cart) == 0: #if there are no items in user cart
                    print("You have nothing in your cart.")
                else: #if there is something in user's cart
                    for fruit, amount in user_cart.items(): #print all items and quantities in user's cart
                        print(f"{fruit} : {amount}")
                    user_item_remove = input("Which item do you want to remove: ") #asks user which item to remove
                    if user_item_remove.capitalize() in user_cart: #checks if user has that item in their cart
                        user_item_remove_amount = input("How many would you like to remove: ") #asks user how many item to remove
                        if user_item_remove_amount.isdigit():
                            user_item_remove_amount = int(user_item_remove_amount)
                            if user_item_remove_amount > user_cart[user_item_remove.capitalize()]: #checks if user has enought items to remove
                                print("You don't have that many items in your cart.")
                            else: #if user has enough items to remove
                                user_cart[user_item_remove.capitalize()] = user_cart[user_item_remove.capitalize()] - user_item_remove_amount
                                print(user_item_remove_amount)
                                print(user_cart)
                                fruit_price = float(fruits[user_item_remove.capitalize()]) #takes price of item to be removed
                                user_item_remove_amount = int(user_item_remove_amount) 
                                item_total = user_item_remove_amount * fruit_price #calculates item remove total
                                cart_total = cart_total - item_total #subracts removed price from total
                                print(cart_total) #prints new total
                        else:
                            print("Please enter amount in digits.")
                    else:
                        print("You don't have that item in your cart.")
            elif user_option == "3":
                print(f"Your total is ${cart_total}") #prints user total
                quit() #quits code
            elif user_option == "4":
                print("You have exited the program.")
                quit() #quits code
        else:
            print("Please enter your choice in digits: ")
    except ValueError:
        print("An error has occured.") #prints if error occurs

