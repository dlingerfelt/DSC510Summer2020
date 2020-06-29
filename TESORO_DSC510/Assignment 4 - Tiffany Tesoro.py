#DSC 510

#Week 4

#Programming Assignment Week 4

#Author Tiffany Tesoro

#06/28/2020

print()
print()

#USER GREETING MESSAGE
print("Welcome to the SoCal Fiber Optic Cable Installation Calculator.")

#RETRIEVAL OF USER AND COMPANY NAME
name = input ("What is your name?\n")
company = input("What is the name of your company?\n")
def greeting():
    print("Nice to meet you " + name + " from " + company +".")

#CALL TO GREETING FUNCTION
greeting()

#RETRIEVAL OF CABLE LENGTH
try:
    feet = float(input("How many feet of fiber optic cable will be installed?\n"))
except:
    feet = float(input("Please try again. Enter a number like 123, 123.4, etc.\n"))

#PRICING FUNCTION DEFINITION
def pricing (feet):
    if feet > 500:
        price = 0.50 # in US Dollars
    elif feet > 250:
        price = 0.70 # in US Dollars
    elif feet > 100:
        price = 0.80 # in US Dollars
    else:
        price = 0.87 # in US Dollars
    return price

#PRICE NOTIFICATION
print()
print()
print("Calculating...")
price = pricing (feet)
if price < 0.87:
    print("Based on length, a bulk discount has been applied.")
else:
    print("Your calculated cost of installation is $0.87 per feet.")

#COST FORMULA FUNCTION DEFINITION
def cost_formula (feet, price):
    installation_cost = feet * price
    return str(format(installation_cost, '.2f'))

#USER RECEIPT PRINT
print()
print()
#COMPANY NAME
print("--Installation Cost for " + company +"--")
#NUMBER OF FEET OF FIBER TO BE INSTALLED
print("Length of fiber optic cable: " + str(format(feet, '.2f')) + " feet")
#CALL TO PRICING FUNCTION
print("Calculated cost of installation: $" + str(format(pricing(feet), '.2f')) + " per foot")
#CALL TO COST FORMULA FUNCTION
print("Total cost of installation: $" + cost_formula(feet, price))

#USER FAREWELL MESSAGE
print()
print()
print("Thank you " + name + " for using the SoCal Fiber Optic Cable Installation Calculator. Enjoy the rest of your day!")
