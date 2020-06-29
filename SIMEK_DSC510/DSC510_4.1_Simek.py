# Katie Simek
# DSC510-T303
# Assignment 4.1
# 28/6/2020

"""
    This program asks the user for their company name, length of fiber
    optic cable to be installed and then computes the cost.
    There is a bulk discount for purchases over 100 feet.
    0-100 = $.87/foot
    101-250 = $.80/foot
    251-500 = $.70/foot
    501+ = $.50/foot
    The program prints a receipt for the user.
"""


def main():
    def install_cost(length, cost):
        return "${:,.2f}".format(cost * length)

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

    # Using conditional statements to determine cost based on length.
    if length <= 100:
        cost = 0.87
    elif 100 < length <= 250:
        cost = 0.80
    elif 250 < length <= 500:
        cost = 0.70
    else:
        cost = 0.50

# printing receipt
    print()
    print()
    print('RECEIPT for:')
    print(company)
    print('Length of fiber optic cable to be installed: ', length, ' feet')
    if length > 100:
        print('**A bulk discount has been applied to your per foot cost.**')
    print('Calculated cost: ', length, ' feet at',
          "${0:.2f}".format(cost), ' per foot')
    print('Total cost of installation: ', install_cost(length, cost))


if __name__ == "__main__":
    main()
