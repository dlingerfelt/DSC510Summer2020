#Assignment 4.1
#Sarah Holdman
#DSC510 Intro to Programming
#6/28/20

#This program will do the following:
#Display a welcome message
#Include a function with two parameters
#Include a call to the function
#Evaluate the cost
#Display the calculated information

#Retrieve company name
company = input('Welcome! Which company are you shopping for?\n')
print('Thank you for shopping for: '+ company)

#Tell about possible discounts
print('Bulk discount can apply to your order:')
print('501+ feet is $0.50/foot')
print('251-500 feet is $0.70/foot')
print('101-250 feet is $0.80/foot')
print('0-100 feet is $0.87/foot')
print()

#Create the cost function
def cost(a,b):
    answer = a * b
    return '$''{0:.2f}'.format(answer)

#Ask for number of feet requested
feet = int(input('How many feet of fiber optic cable do you need?\n'))

#Create variable for prices
if feet >= 501:
    price = 0.50
elif feet >= 251:
    price = 0.70
elif feet >= 101:
    price = 0.80
else:
    price = 0.87

#Display the total cost
print(feet, 'feet will cost', cost(feet,price))
print()

#Display a receipt
print('Receipt')
#Display company name
print('Purchased by:', company)
#Display feet requested
print('Feet requested:', feet)
#Display price per foot with discount
print('Price per foot:', '$''{0:.2f}'.format(price))
#Display the total cost
print('The total cost for your order is', cost(feet,price))
