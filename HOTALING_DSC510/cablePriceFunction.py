# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Michael Hotaling
# 06/24/2020


def price_calculation(feet):
    # Price Calculation. This function checks to see if the user is eligible for a bulk discount
    # We have three different discounts, > 500ft, >250ft and >100ft
    # We've added abs() in the function just in case the user needs to return some cable
    if abs(feet) > 500:
        return 0.50
    elif abs(feet) > 250:
        return 0.70
    elif abs(feet) > 100:
        return 0.80
    else:
        return 0.87


def regular_price():
    # We can declare the standard price here so we can call it later when checking how much money the user saved
    # This can be helpful if the standard price ever changes
    return 0.87


def bill(feet, price):
    # Bill calculator. This function multiplies the amount of feet by the price of the cable per foot to get the
    # total price
    return feet * price


def input_cable_length():
    # Create the function to ask the user for how many feet of fiber they need
    # There is error handling, but if the input triggers an error, the program is terminated
    try:
        length = float(input('How many feet of fiber optic cable is required?: '))
        return length
    except ValueError:
        print("Oops! Please put in a numerical value. eg. 55, 3.14, 9999")
        print("Please try again!")
        exit()


def main():
    # Introduction
    print('Hello! Welcome to the Fiber Optic Price Calculator!')

    # Asking the user which company they are from
    company = input('Which company are you from?: ')
    print("Okay! You are from " + company + ". That's great to hear!")

    # Use the input_cable_length() function to ask the user how many feet of cable they need
    fiber_length = input_cable_length()

    # We will check for the price per length of cable here
    # If the user requests more than a certain amount of cable, they will get a discount
    fiber_price = price_calculation(fiber_length)
    total_cost = bill(fiber_length, fiber_price)

    # This is just a fun little message to let the user know they are getting our bargain pricing
    if fiber_price != 0.87 and fiber_length > 0:
        print("Good news! You're eligible for our bulk discount!")

    # We are using the correct formatting now for the price format
    if fiber_length < 0:
        print('Oh! Okay! You need to return ' + str(-fiber_length) + ' feet of fiber cable. We will credit you ' +
              f'${-total_cost:,.2f}'.replace('$-', '-$'))
    elif fiber_length == 0:
        print("Don't need any cable today? That's okay! We are always open! ")
    else:
        print('You will need {0} feet of fiber optic cable! That will cost you ${1}'.format(str(fiber_length), (
            f'${total_cost:,.2f}'.replace('$-', '-$'))))

    # Some print statements to create some room between the chat and the receipt
    print()

    # Printing the receipt
    print("--" + company + " Cable Company--")
    print("--Fiber Optic Receipt--")
    print("--Feet of Cable: " + str(fiber_length) + "--")
    print("--Price per Foot: " + (f'${fiber_price:,.2f}'.replace('$-', '-$')) + "--")
    print("--Total Cost: " + (f'${total_cost:,.2f}'.replace('$-', '-$')) + "--")

    if fiber_price != 0.87 and fiber_length > 0:
        print("--You saved " + (f'${fiber_length * regular_price() - total_cost :,.2f}'.replace('$-', '-$')) +
              " with our discount!--")
    print("--Please come again soon!--")

if __name__ == "__main__":
    main()
