#DSC 510
#Week 2
#Programming Assignment 2.1
#Sarah Holdman
#06/12/20

#This program will do the following:
#Display a welcome message
#Retrieve the company name
#Retrieve the number of feet of cable needed
#Calculate the cost of installation
#Print a receipt

#Welcome user and retrieve company name
company = input('Welcome! Which company are you shopping for?\n')
#Ask for the number of feet needed
feet = input('How many feet of fiber optic cable do you need?\n')
#Convert string to an integer
feet = int(feet)
#Create a variable for the price
price = 0.87
#Determine cost by multiplying feet by price
cost = (feet) * (price)
#Display the total cost
print('For this much fiber optic cable it will cost:')
print(cost)
#Display a receipt
print('Receipt:')
#Display company name
print(company)
#Display feet requested
print('Feet requested:')
print(feet)
#Display price per foot
print('Price per foot:')
print(price)
#Display the total cost
print('Total cost:')
print(cost)
