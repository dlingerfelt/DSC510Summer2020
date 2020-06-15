#DSC 510

#Week 2

#Programming Assignment Week 2

#Author James Mulvihill

#06/12/2020


#Display welcome message
print("Welcome to the Fiber Optic Cable company!")

#Get the company name
company_name = input("Name of company: ")

#Get the number of feet
feet = input("Feet of fiber optic cable to be installed: ")

#Calculate the cost
cost = float(feet) * .87

#Print the receipt
print("\nCompany Name: " +  company_name)
print("Number of feet needed: " + feet)
print("Cost: ${:.2f}".format(cost))

