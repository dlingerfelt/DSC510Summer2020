# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Michael Hotaling
# 06/16/2020


def price_calculation(feet):
    # Bulk Discount Function. This function checks to see if the user is eligible for a bulk discount
    # We have three different discounts, > 500ft, >250ft and >100ft
    if feet > 500:
        return 0.50
    elif feet > 250:
        return 0.70
    elif feet > 100:
        return 0.80
    else:
        return 0.87


def bill(feet, price):
    # Total Cost Calculator. This function multiplies the amount of feet by the price of the cable per foot to get the
    # total price
    return feet * price


def main():
    # Introduction
    print('Hello! Welcome to the Fiber Optic Price Calculator!')

    # Asking the user which company they are from
    # Convert the company name to a string in case it is something like "101" Cable Company
    company = str(input('Which company are you from?: '))
    print("Okay! You are from " + company + ". That's great to hear!")

    # Asking the user how many feet of cable they will need for their job
    # There is no error handling here, so if a string is passed, it will break the program
    fiber_length = float(input('How many feet of fiber optic cable is required?: '))

    # We will check for the price per length of cable here
    # If the user requests more than a certain amount of cable, they will get a discount

    fiber_price = price_calculation(fiber_length)
    total_cost = bill(fiber_length, fiber_price)

    if fiber_price != 0.87:
        print("Good news! You're eligible for our bulk discount!")

    # We are using the correct formatting now for the price format
    print('You will need ' + str(fiber_length) + ' feet of fiber optic cable! That will cost you $' + (
        f'${total_cost:,.2f}'.replace('$-', '-$')))

    # Some print statements to create some room between the chat and the receipt
    print()

    # Printing the receipt
    print("--" + company + " Cable Company--")
    print("--Fiber Optic Receipt--")
    print("--Feet of Cable: " + str(fiber_length) + "--")
    print("--Price per Foot: " + (f'${fiber_price:,.2f}'.replace('$-', '-$')) + "--")
    print("--Total Cost: " + (f'${total_cost:,.2f}'.replace('$-', '-$')) + "--")

    if fiber_price != 0.87:
        print("--You saved " + (f'${fiber_length * 0.87 - total_cost :,.2f}'.replace('$-', '-$')) +
              " with our discount!--")


if __name__ == "__main__":
    main()
