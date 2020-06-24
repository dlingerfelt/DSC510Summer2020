#DSC 510
#Week 3
#Programming Assignment 3.1
#Sarah Holdman
#06/21/2020

#This program will do the following:
#Display a welcome message
#Get the company name
#Give the number of feet of cable
#Evaluate the cost
#Display the calculated information

#Retrieve the company name
company = input('Welcome! Which company are you shopping for?\n')

#Tell the customer about possible discounts
print('Bulk discount can apply to your order')
print('501+ feet is $0.50/foot')
print('251-500 feet is $0.70/foot')
print('101-250 feet is $0.80/foot')
print('0-100 feet is $0.87/foot')

#Retrieve the number of feet desired
feet = float(input('How many feet of fiber optic cable do you need?\n'))

#Create variable for prices
if feet >= 501:
    price = 0.50
elif feet >= 251:
    price = 0.70
elif feet >= 101:
    price = 0.80
else:
    price = 0.87

#Multiply feet by price
cost = float(price * feet)

#Convert price format
price = '{0:.2f}'.format(price)
price = '$' + str(price)

#Convert cost format
cost = '{0:.2f}'.format(cost)
cost = 'The total cost is $' + str(cost)

#Display the total cost
print(cost)

#Display a receipt
print('Receipt')
#Display company name
print(company)
#Display feet requested
print('Feet requested')
print(feet)
#Display price per foot
print('Price per foot')
print(price)
#Display the total cost
print(cost)
