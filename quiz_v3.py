from easygui import*

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
options_list_string = "\n".join(options_list)

#makes the user's cart a dictionary
user_cart = {}

#sets the user's cart total to 0 
cart_total = 0
#sets the user's budget to 0
user_budget = 0

#function to search user's cart to see if it already has that item
def search_cart(user_cart, item):
    if item in user_cart:
        return user_cart[item]
    return None

#function to add items and calculate new total
def add_item(fruit, quantity, price_list):
    global cart_total
    fruit_price = price_list[fruit.capitalize()]
    fruit_price = float(fruit_price)
    fruit_choice_amount = int(quantity)
    item_total = fruit_choice_amount * fruit_price
    cart_total = cart_total + item_total
    msgbox(f"Your total is now ${cart_total}.")

#function to add the item to the code dictionary
def add_item_user_cart():
    if user_item_amount is not None:
        user_cart[fruit_choice.capitalize()] = fruit_choice_amount + user_item_amount
    else:
        user_cart[fruit_choice.capitalize()] = fruit_choice_amount

#function to remove items from the user's cart
def remove_item_user_cart(user_cart):
    global updated_cart_total
    if len(user_cart) == 0: #checks if the cart is empty
        msgbox("You have nothing in your cart.")
    else:
        msgbox("\n".join(f"{item}: {quantity}" for item, quantity in user_cart.items())) #prints the items and quantities of the user's cart
        user_item_remove = enterbox("Which item do you want to remove: ") #asks the user what they want to remove
        if user_item_remove.capitalize() in user_cart: #checks if what the user entered is in their cart
            user_item_remove_amount = enterbox("How many would you like to remove: ") #asks the user how many of that item to remove
            if user_item_remove_amount.isdigit(): #checks if the user's input is a digit
                user_item_remove_amount = int(user_item_remove_amount)
                user_cart_amount = int(user_cart[user_item_remove.capitalize()])
                if user_item_remove_amount > user_cart_amount: #checks if user has enought items to remove
                    print("You don't have that many items in your cart.")
                else: #if user has enough items to remove
                    user_cart[user_item_remove.capitalize()] = user_cart_amount - user_item_remove_amount
                    fruit_price = float(fruits[user_item_remove.capitalize()]) #takes price of item to be removed
                    user_item_remove_amount = int(user_item_remove_amount) 
                    item_total = user_item_remove_amount * fruit_price #calculates item remove total
                    updated_cart_total = cart_total - item_total #subracts removed price from total
            else:
                msgbox("Please enter amount in digits.")
        else:
            msgbox("You don't have that item in your cart.")

#function to check whether user has gone over budget
def budget_check():
    if cart_total > user_budget: #checks if the user's total is greater than the budget
        msgbox("Your total is now over your inital budget")
    else:
        pass #skips the code

#while loop continue or end code
while True:
    start = enterbox("Do you want to start the shopping cart program? Yes or No: ") #asks the user if they want to start
    if start == "yes" or start == "no": #check if the user's input is "yes" or "no"
        if start.lower() == "yes":
            break #breaks the while loop to continue code
        elif start.lower() == "no": #quits the code
            msgbox("You have exited the quiz")
            quit()
    else:
        msgbox("Please enter Yes or No")

#while loop for user's name
while True:
    user_name = enterbox("Please enter your name: ") #asks users to enter their name
    if user_name is None:
        msgbox("Please enter your name")
    else:
        if user_name.isalpha(): #prints the name of the user and welcome
            msgbox(f"*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n \n Welcome {user_name.capitalize()}! \n \n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            break #breaks the while loop to continue code
        else:
            msgbox("Please enter your name in alphabetical format") #asks user to re-enter their name in alphabets

#while loop for user's budget
while True:
    user_budget = enterbox("Please enter your budget in $NZD: ") #asks user for their budget
    if user_budget is None:
        msgbox("Please enter a budget")
    else:
        if user_budget.isdigit(): #checks if the user's input was a digit
            user_budget = int(user_budget)
            msgbox(f"Your user budget is set to ${user_budget}")
            break
        else:
            msgbox("Please enter your budget in digits") #asks user to re-enter their input as a digit

#while loop to ask user what they want to do
while True:
    try:
        user_option = enterbox(f"{options_list_string} \n\nPlease enter what you want to do next with the corresponding number \n\nEnter number: ")#asks the user what they want to do and prints options
        if user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4": #checks if user input is 1, 2, 3, or 4
            if user_option == "1": #runs the option to add items
                while True: #loops back to the fruit input menu
                    msgbox("\n".join(f"{fruit}: {price}" for fruit, price in fruits.items())) #prints the list of fruits and their prices
                    fruit_choice = enterbox("Please enter which fruit you would like: \n\n(Apple, Orange, Banana, Grape, Blueberry)") #asks the user what item to add
                    if fruit_choice is None:
                        msgbox("Please enter a fruit")
                    else:
                        if fruit_choice.capitalize() == "Apple" or fruit_choice.capitalize() == "Orange" or fruit_choice.capitalize() == "Banana" or fruit_choice.capitalize() == "Grape" or fruit_choice.capitalize() == "Blueberry":
                            fruit_choice_amount = enterbox("How many would you like: ") #asks user how many to add
                            if fruit_choice_amount.isdigit(): #checks if user's input is a digit
                                add_item(fruit_choice, fruit_choice_amount, fruits) #calls function to add item and update cart total
                                item = fruit_choice.capitalize()
                                user_item_amount = search_cart(user_cart, item) #calls function to check if the user already has this item in their cart
                                add_item_user_cart() #calls function to add item to user cart
                                budget_check() #checks if the user has gone over budget
                                break
                            else:
                                msgbox("Please enter your input in digits") #asks the user to re-enter their input as digits
                        else:
                            msgbox("Please enter your answer again.")
            elif user_option == "2": #runs the option to remove items
                remove_item_user_cart(user_cart) #calls function to remove items
                cart_total = updated_cart_total
                msgbox(f"Your cart total is now ${cart_total}")
            elif user_option == "3": #runs the option to display user total and end code
                msgbox(f"Your total is ${cart_total}")
                quit()
            elif user_option == "4": #runs the option to completely quit the program
                msgbox("You have exited the program.")
                quit()
        else:
            msgbox("Please enter your choice in digits: ") #asks the user to re-enter their answer in digits
    except ValueError:
        msgbox("An error has occured.") #prints if error occurs

