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

#makes the user's cart a dictionary
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

#function to add items to cart
def add_item(fruit, quantity, price_list):
    global cart_total
    fruit_price = price_list[fruit.capitalize()] #takes the price of the item
    fruit_price = float(fruit_price) #converts price to float
    fruit_choice_amount = int(quantity)
    item_total = fruit_choice_amount * fruit_price #calculates total item price of all added items
    cart_total = cart_total + item_total #adds item price to user total
    print(f"Your total is now ${cart_total}.") #prints user total

#function to add the item to the dictionary user_cart
def add_item_user_cart(): #calls function to check if the user already has that item in their cart
    if user_item_amount is not None: #if user already has the item
        user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount #only add the the item quantity
    else: #if user doesn't have the item
        user_cart[fruit_choice.capitalize()] = fruit_choice_amount #add the item and quanity to the cart

#function to remove items from user's cart
def remove_item_user_cart(user_cart):
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
                    return cart_total
            else:
                print("Please enter amount in digits.")
        else:
            print("You don't have that item in your cart.")

#function to check if user has gone over budget
def budget_check():
    if cart_total > user_budget:
        print("Your total is now over your inital budget")
    else:
        pass

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

while True:
    user_budget = input("Please enter your budget in $NZD: ")
    if user_budget.isdigit():
        user_budget = int(user_budget)
        print(f"Your user budget is set to {user_budget}")
        break
    else:
        print("Please enter your budget in digits")

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
        
        if user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4": #checks if the user input is one of the 4 options
            if user_option == "1":
                print("Here are the options for Fruits: ")
                for fruit, price in fruits.items():
                    print(f"{fruit} : ${price}")
                fruit_choice = input("Please enter which fruit you would like (Apple, Orange, Banana, Grape, Blueberry): ") #asks which fruit the user wants to add
                if fruit_choice.capitalize() == "Apple" or fruit_choice.capitalize() == "Orange" or fruit_choice.capitalize() == "Banana" or fruit_choice.capitalize() == "Grape" or fruit_choice.capitalize() == "Blueberry":
                    fruit_choice_amount = input("How many would you like: ") #asks the user how many they want
                    if fruit_choice_amount.isdigit(): #checks if user's input is a digit
                        add_item(fruit_choice, fruit_choice_amount, fruits) #calls function to add item and update cart total
                        item = fruit_choice.capitalize()
                        user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has this item in their cart
                        add_item_user_cart() #calls function to add item to user cart
                        budget_check() #checks if the user has gone over budget
                    else:
                        print("Please enter your input in digits")
                else:
                    print("Please enter your answer again.")
            elif user_option == "2":
                remove_item_user_cart(user_cart)
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

