from easygui import*
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

#sets the price for each fruit
fruits = {"Apple":"0.50",
          "Orange":"1.00",
          "Banana":"4.30",
          "Grape":"12.99",
          "Blueberry":"6.99"}

#creates a variable for a fruits list to be used in choicebox
fruits_list = []

#adds all the items from the fruits dictionary to the list
for fruit, price in fruits.items():
    fruits_list.append(fruit)

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

#sets the buttonbox constant of yes no
yes_no = ["Yes", "No"]
#sets the buttonbox constant of 1, 2, 3, and 4
number_options = ["1", "2", "3", "4"]

#sets all the parameters for multenterbox for user details
title = "User Login" 
msg = "Enter your account details" 
fieldNames = ["Username", "Password"]

#JSON file to store user's data
accounts_file = "accounts_file.json"

#sets the buttonbox constants for login page
account_load_options = ["Sign Up", "Login", "Exit"]

#sets the colours for the data visualization
colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "White"]

#function to search user's cart to see if it already has that item
def search_cart(user_cart, item):
    if item in user_cart:
        return user_cart[item]
    return None

#Function to load user details from file
def load_user():
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as acc_file:
            return json.load(acc_file)
    return {}

#Function to save user details to file
def save_user(user):
    with open(accounts_file, "w") as save_file:
        json.dump(user, save_file, indent=4)

#function to login and signup
def login():
    global user_name
    user = load_user()
    while True:
        account_load = buttonbox("Do you want to sign up or login?", "Login", account_load_options) #asks user if they want to sign up or login or exit
        if account_load is not None:
            if account_load == "Sign Up": #checks if user clicks sign up
                while True:
                    fieldValues = multenterbox(msg, title, fieldNames) #creates a multi-enterbox for users to enter thier details.
                    if fieldValues is not None: #checks is all fields have been entered
                        for i in range(len(fieldNames)): #for loop to check each field
                            if fieldValues[i].strip() == "": #checks if field is empty or not
                                fieldValues = multenterbox(f"{msg}\n*Please do not leave any fields empty", title, fieldNames) #asks user to fill in each field
                        user_name, password = fieldValues #assigns all field values a variable name
                        if user_name in user: #if user inputs existing username
                            msgbox("This username already exists. Please try logging in.")
                        else:
                            pass_confirm = enterbox("Confirm your password:") #asks user to confirm password if user enters new username
                            if pass_confirm is not None: #if user exits program 
                                if pass_confirm != password: #if user enters password which doesn't match with first passoword
                                    msgbox("Passwords entered do not match. Please try again.")
                                else:
                                    user[user_name] = {"password": password, "cart": {}}
                                    save_user(user) #adds new user to json file
                                    msgbox("Account created successfully") #lets user know that account has been created
                                    return user_name #exits the whole function and sends the user_name value back to the code.
                            else:
                                msgbox("You have cancelled sign-up")
                    else:
                        msgbox("You have cancelled sign-up")
                        break
            elif account_load == "Login": #checks if user clicks login
                while True:
                    fieldValues = multenterbox(msg, title, fieldNames) #creates a multi-enterbox for users to enter thier details
                    if fieldValues is not None: #checks is all fields have been entered
                        for i in range(len(fieldNames)): #for loop to check each field
                            if fieldValues[i].strip() == "": #checks if field is empty or not
                                fieldValues = multenterbox(f"{msg}\n*Please do not leave any fields empty", title, fieldNames) #asks user to fill in each field
                        user_name, password = fieldValues #assigns all field values a variable name
                        if user_name in user and user[user_name]["password"] == password: #if username and password matches to details in file
                            msgbox(f"Welcome back, {user_name}!") #welcomes user to program
                            return user_name
                        else:
                            msgbox("Invalid username or password.") #if username or password is invalid
                    else:
                        msgbox("You have cancelled login")
            elif account_load == "Exit": #checks if user clicks exit
                msgbox("You have exited the program")
                quit()

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
def remove_item_user_cart():
    if len(user_cart) == 0: #checks if the cart is empty
        msgbox("You have nothing in your cart.")
    else:
        while True:
            msgbox("\n".join(f"{item}: {quantity}" for item, quantity in user_cart.items())) #prints the items and quantities of the user's cart
            user_item_remove = enterbox("Which item do you want to remove: ") #asks the user what they want to remove
            if user_item_remove is not None:
                if user_item_remove.capitalize() in user_cart: #checks if what the user entered is in their cart
                    remove_item_user_cart_quant(user_item_remove)
                    break
                else:
                    msgbox("You don't have that item in your cart.")
            else:
                break

                user_item_remove_amount = int(user_item_remove_amount)
                user_cart_item = int(user_cart[user_item_remove.capitalize()])
                if user_item_remove_amount > user_cart_item: #checks if the user has that many items in their cart
                    msgbox("You don't have that many items in your cart.")
                else:
                    fruit_price = float(fruits[user_item_remove.capitalize()])
                    item_total = user_item_remove_amount * fruit_price #finds the total cost of the items to be removed
                    cart_total = cart_total - item_total #subracts the removed item's cost from the old cart total
                    return cart_total #updates the cart total

def remove_item_user_cart_quant(user_item_remove):
    while True:
        global updated_cart_total
        user_item_remove_amount = enterbox("How many would you like to remove: ") #asks the user how many of that item to remove
        if user_item_remove_amount is not None:
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
                    break
            else:
                msgbox("Please enter amount in digits.")
        else:
            break

#function to check whether user has gone over budget
def budget_check():
    if cart_total > user_budget: #checks if the user's total is greater than the budget
        msgbox("Your total is now over your inital budget")
    else:
        pass #skips the code

#function to display user's cart with data visualization
def data_vis(user_cart_file):
    with open("usercart_dv.txt", "w") as dv_file:
        dv_file.write("Item,Quantity")
        for item, quantity in user_cart_file.items():
            dv_file.write(f"\n\n{item},{quantity}")
    fruits_dv = pd.read_csv('usercart_dv.txt') #load user cart
    fruits_dv.plot(x = 'Item', y = 'Quantity', kind = "bar", color = colours) #plots a bar graph of items bought
    plt.show() #shows the plot

#function to print the user's final total and receipt
def prt_receipt():
    with open("prt_receipt_file.txt","w") as file: #writes to a different file which only contains the most recent data
        file.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        file.write(f"\nUsername: {user_name}\n")
        for item, quantity in user_cart.items():
            fruit_price = fruits[item.capitalize()]
            fruit_price = float(fruit_price)
            quantity = int(quantity)
            item_total = quantity * fruit_price
            file.write(f"\nItem: {item}, Quantity: {quantity}x, Cost: ${item_total}")
        file.write("\n\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    with open ("prt_receipt_file.txt","r") as prt_file: #seperate exeternal file for printing only the most recent data
        print_file = prt_file.read()
        msgbox(print_file)

#while loop continue or end code
while True:
    start = buttonbox("Do you want to start the shopping cart program? Yes or No: ", "Start", yes_no) #asks the user if they want to start
    if start is not None:
        if start.lower() == "yes": #check if the user's input is "yes" or "no"
            break #breaks the while loop to continue code
        elif start.lower() == "no": #quits the code
            msgbox("You have exited the quiz")
            quit()
    else:
        msgbox("You have exited the quiz")
        quit()

#calls function to login
login()

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
        user_option = buttonbox(f"{options_list_string} \n\nPlease enter what you want to do next with the corresponding number \n\nEnter number: ", "Options", number_options)#asks the user what they want to do and prints options
        if user_option is not None:
            if user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4": #checks if user input is 1, 2, 3, or 4
                if user_option == "1": #runs the option to add items
                    while True: #loops back to the fruit input menu
                        msgbox("\n".join(f"{fruit}: {price}" for fruit, price in fruits.items())) #prints the list of fruits and their prices
                        fruit_choice = choicebox("Click which fruit you want to add", "Fruits", fruits_list) #asks the user what item to add
                        if fruit_choice is None: #checks if user has entered
                            msgbox("Please enter a fruit")
                        else:
                            if fruit_choice.capitalize() == "Apple" or fruit_choice.capitalize() == "Orange" or fruit_choice.capitalize() == "Banana" or fruit_choice.capitalize() == "Grape" or fruit_choice.capitalize() == "Blueberry":
                                fruit_choice_amount = enterbox(f"How many would you like: \n\n Item: {fruit_choice}    Price : ${fruits[fruit_choice]}") #asks user how many to add
                                if fruit_choice_amount is not None:
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
                                    msgbox("Please enter an amount.")
                            else:
                                msgbox("Please enter your answer again.")
                elif user_option == "2": #runs the option to remove items
                    remove_item_user_cart() #calls function to remove items
                    cart_total = updated_cart_total
                    msgbox(f"Your cart total is now ${cart_total}")
                elif user_option == "3": #runs the option to display user total and end code
                    prt_receipt()
                    data_vis(user_cart)
                    msgbox("Thank you for shopping with us!\n\n Have a great day!")
                    quit()
                elif user_option == "4": #runs the option to completely quit the program
                    msgbox("You have exited the program.")
                    quit()
            else:
                msgbox("Please enter your choice in digits: ") #asks the user to re-enter their answer in digits
        else:
            msgbox("You have exited the quiz")
            quit()
    except ValueError:
        msgbox("An error has occured.") #prints if error occurs
