#DSC 510

#Week 3

#Programming Assignment Week 3

#Author Tiffany Tesoro

#06/21/2020

print()
print()

#USER GREETING MESSAGE
print("Welcome to the Riverside Fiber Optic Cable Installation Calculator.")

#RETRIEVAL OF USER AND COMPANY NAME
name = input ("What is your name?\n")
print()
print("Nice to meet you " + name +".")
company = input ("What is the name of your company?\n")

#RETRIEVAL OF CABLE LENGTH
print()
print("Great! Now " + name + " from " + company +",")
try:
    cable_length = float(input("How many feet of fiber optic cable will be installed?\n"))
except:
    cable_length = float(input("Please try again. Enter a number like 123, 123.4, etc.\n"))

#INSTALLATION COST CALCULATION
print()
print()
print("Calculating...")
#PRICE OF INSTALLATION PER FEET
if cable_length > 500:
    calculated_cost = 0.50 #in US Dollars
elif cable_length > 250:
    calculated_cost = 0.70 #in US Dollars
elif cable_length > 100:
    calculated_cost = 0.80 #in US Dollars
else:
    calculated_cost = 0.87 #in US Dollars
#PRICE NOTIFICATION
if calculated_cost < 0.87:
    print("Based on length, a bulk discount has been applied.")
else:
    print("Your calculated cost of installation is $0.87 per feet.")
#COST FORMULA
installation_cost = cable_length * calculated_cost

#USER RECEIPT PRINT
print()
print()
#COMPANY NAME
print("--Installation Cost for " + company +"--")
#NUMBER OF FEET OF FIBER TO BE INSTALLED
print("Length of fiber optic cable: " + str(cable_length) + " feet")
#CALCULATED COST
print("Calculated cost of installation: $" + str(format(calculated_cost, '.2f')) + " per foot")
#TOTAL COST
print("Total cost of installation: $" + str(format(installation_cost, '.2f')))

#USER FAREWELL MESSAGE
print()
print()
print("Thank you " + name + " for using the Riverside Fiber Optic Cable Installation Calculator. Enjoy the rest of your day!")