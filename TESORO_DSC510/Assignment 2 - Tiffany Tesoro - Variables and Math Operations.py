#DSC 510

#Week 2

#Programming Assignment Week 2

#Author Tiffany Tesoro

#06/14/2020

print()
print()

#USER GREETING MESSAGE
print("Welcome to the California Fiber Optic Cable Installation Calculator.")

#RETRIEVAL OF USER AND COMPANY NAME
name = input ("What is your name?\n")
print()
print("Nice to meet you " + name +".")
company = input ("What is the name of your company?\n")

#RETRIEVAL OF CABLE LENGTH
print()
print("Great! Now " + name + " from " + company +",")
cable_length = float(input ("How many feet of fiber optic cable will be installed? Ex. 123, 45.6, 789.01, etc.\n"))

#INSTALLATION COST CALCULATION
print()
print()
print("Calculating...")
#Price of Installation Per Feet
calculated_cost = 0.87 #in US Dollars
#Cost Formula
installation_cost = cable_length * calculated_cost

#USER RECEIPT PRINT
print()
print()
#COMPANY NAME
print("--Installation Cost for " + company +"--")
#NUMBER OF FEET OF FIBER TO BE INSTALLED
print("Length of fiber optic cable: " + str(cable_length) + " feet")
#CALCULATED COST
print("Calculated cost of installation: $" + str(calculated_cost) + " per foot")
#TOTAL COST
print("Total cost of installation: $" + str(format(installation_cost, '.2f')))

#USER FAREWELL MESSAGE
print()
print()
print("Thank you " + name + " for using the California Fiber Optic Cable Installation Calculator. Have a great day!")