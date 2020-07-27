# Katie Simek
# DSC510-T303
# Assignment 5.1
# 5/7/2020

"""
    This program asks the user which mathematical operation they
    would like to perform or if they want to average numbers.
    The program continues until the user terminates the program.
"""


# Performs the math operation based on user entered operation.
def perform_calculation(operation):
    # Validates user entered math symbol or returns error.
    while True:
        if operation == '*' or '/' or '+' or '-':
            break
        else:
            print('Error.  Please enter a valid mathematical operation.')
            continue
    # Validates input can be converted to an float or returns error.
    while True:
        try:
            number1 = float(input('Enter the first number: '))
            break
        except ValueError:
            print('Invalid entry.  Please enter the first number.')
            continue
    # Validates input can be converted to an float or returns error.
    while True:
        try:
            number2 = float(input('Enter the second number: '))
            break
        except ValueError:
            print('Invalid entry.  Please enter a number.')
            continue
    # Conditional to prevent zero division error.
    if operation == '/' and number2 == 0:
        print('Invalid entry.  Cannot divide by zero.')
    # Mathematical operations.
    if operation == '*':
        return number1 * number2
    if operation == '/':
        return number1 / number2
    if operation == '+':
        return number1 + number2
    if operation == '-':
        return number1 - number2


# Calculates average of user specified number of values.
def calculate_average():
    # Asking for number of values to be averaged.
    quantity = int(input('How many values would you like to average? '))
    # Initializing loop to zero, setting sum of the values to zero.
    q = 0
    sum_num = 0
    # Loop to iterate through values for the number of times entered
    # by user, asking for values each time.
    while q < quantity:
        number = float(input('Enter a number:  '))
        sum_num = sum_num + number
        q += 1
    return sum_num / quantity


def main():
    # Asks user for the purpose of the entry.
    while True:
        action = input('What type of operation would you like to perform?\n'
                       '    Enter "1" for mathematical calculation.\n'
                       '    Enter "2" to calculate the average of numbers.\n'
                       '    Enter "3" to terminate the program.\n')
        # Asks for mathematical operation then calls calculation function.
        if action == str('1'):
            operation = input('Please enter the mathematical operation you'
                              ' would like to perform:\n'
                              '    "*" for multiplication\n'
                              '    "/" for division\n'
                              '    "+" for addition\n'
                              '    "-" for subtraction \n')
            print(perform_calculation(operation))
            continue
        # Call average function
        if action == str('2'):
            print(calculate_average())
            continue
        # Print closing statement and terminate program.
        if action == str('3'):
            print("Program Complete.")
            break
        # Return error for invalid entry.
        else:
            print('**** Invalid entry. ****\n')
            continue


main()
