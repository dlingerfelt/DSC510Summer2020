# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Michael Hotaling
# 06/12/2020


# Bulk Discount Function. This function checks to see if the user is eligible for a bulk discount
def bulk_discount(feet):
	if feet > 500:
		return 0.50
	elif feet > 250:
		return 0.70
	elif feet > 100:
		return 0.80
	else:
		return 0.87


# Total Cost Calculator. This functon multiplies the amount of feet by the price of the cable per foot to get the
# total price

def total_cost(feet, price):
	return feet * price


# Introduction
print('Hello! Welcome to the Fiber Optic Price Calculator!')

# Asking the user which company they are from
# Convert the company name to a string in case it is something like "101" Cable Company
company = input('Which company are you from?: ')
print("Okay! You are from " + str(company) + ". That's great to hear!")

# Asking the user how many feet of cable they will need for their job
# There is no error handling here, so if a string is passed, it will break the program
fiberLength = float(input('How many feet of fiber optic cable is required?: '))

# We will check for the price per length of cable here
# If the user requests more than a certain amount of cable, they will get a discount

fiberPrice = bulk_discount(fiberLength)
totalCost = total_cost(fiberLength, fiberPrice)

if fiberPrice != 0.87:
	print("Good news! You're eligible for our bulk discount!")


# We will need to round the total price to prevent float issues
print('You will need ' + str(fiberLength) + ' feet of fiber optic cable! That will cost you $' + (f'${totalCost:,.2f}'.replace('$-', '-$')))

# Some print statements to create some room between the chat and the receipt
print()
print()

# Printing the receipt
print("--" + company + " Cable Company--")
print("--Fiber Optic Receipt--")
print("-Feet of Cable: " + str(fiberLength) + "-")
print("-Price per Foot: " + (f'${fiberPrice:,.2f}'.replace('$-', '-$')) + "-")
print("-Total Cost: " + (f'${totalCost:,.2f}'.replace('$-', '-$')) + "-")
