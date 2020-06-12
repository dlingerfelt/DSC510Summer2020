'''
Fiber Optic Cable installation receipt Generator
Purpose of Program: Generate a automated receipt for fiber optic cable installation program by getting input
                    from user for company name and how much fiber optic cable to be installed,calculate total
                    installation cost and generate receipt for user
Assignment Number : 2.1 Programming Assignment
Name : Dhiraj Bankar
'''

# Define global variable for fiber optic installation cost
fixed_price = 0.87

# Welcome message
print("---Welcome to the fiber optic cable installation program---")

# Retrieve the company name from user
company_name = input("Please enter company name \n")

# Retrieve the no. of feet cable to be installed from user
no_of_feet = input("Please enter the how much fiber optic cable you want (in feet) \n")

# Convert user input to float otherwise calculation will fail
no_of_feet = float(no_of_feet)

# Calculate the final cost installation cost
total_installation_cost = (no_of_feet * fixed_price)

# printing the receipt
print("---Fiber Optic Cable Installation Receipt---")
print("Company Name :", company_name)
print("No of Feet fiber optic cable installed :", no_of_feet)
print("Price per Feet: ", fixed_price)
print("Total Cost :", total_installation_cost)



