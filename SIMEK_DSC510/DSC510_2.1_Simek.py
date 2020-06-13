# Katie Simek
# DSC510-T303
# Assignment 2.1
# 12/6/2020

"""
    This program asks the user for their company name, length of cable
    to be installed and computes the cost at $.87 per foot.
    The program prints a receipt for the user.
"""

print('Hello, welcome to the fiber optic cable installation '
      'cost estimator.')
company = input('Please enter your company name: ')

# Asking for length, verifying input is a number by testing conversion to a float
while True:
    length = input('Enter the number of feet of fiber optic cable to'
                   ' be installed: ')
    try:
        length = float(length)
        break
    except ValueError:
        print('**Invalid entry. **Please enter the length of cable in feet.: ')
    continue

install_cost = "${:,.2f}".format(.87 * length)

print()
print()
print('RECEIPT for:')
print(company)
print('Length of fiber optic cable to be installed: ', length, ' feet')
print('Calculated cost: ', length, ' feet at',
      "${0:.2f}".format(.87), ' per foot')
print('Total cost of installation: ', install_cost)
