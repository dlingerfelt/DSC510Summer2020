# DSC 510

# Week 5

# Programming Assignment Week 5

# Author Tiffany Tesoro

# 07/05/2020

print()

#USER GREETING MESSAGE
print('Welcome to the PyLoops Calculator!')

#UTILIZED WHEN USER WANTS TO END PROGRAM
import sys

#DEFINE REPEAT_MAIN FUNCTION
def repeat_main():
    main()

#DEFINE PERFORM_CALCULATION FUNCTION
def perform_calculation(operation):
    first_number = input('Type in the first number and press enter: \n')
    second_number = input('Type in the second number and press enter: \n')

    a = int(first_number)
    b = int(second_number)

    if operation == '+':
        print(f'The sum of {a} and {b} is equal to {a + b}')
        repeat_main()
    elif operation == '-':
        print(f'The difference between {a} and {b} is equal to {a - b}')
        repeat_main()
    elif operation == '*':
        print(f'The product of {a} and {b} is equal to {a * b}')
        repeat_main()
    elif operation == '/':
        print(f'The quotient of {a} and {b} is equal to {a / b}')
        repeat_main()
    else:
        print('Invalid input. Please try again. \n')
        return

#DEFINE CALCULATE_AVERAGE FUNCTION
def calculate_average():
    while True:
        try:
            quantity = int(input('Type in the quantity of numbers you will average and press enter: \n'))
            break
        except ValueError:
            print('Invalid input. Please try again. \n')
            return
    if quantity > 0:
        input_num = input('Type in all the numbers you would like to average separated by space then press enter: \n')
        list = input_num.split()
        sum = 0
        average = 0
        for num in list:
            sum += int(num)
            average = sum / quantity
        print('The average is equal to: ' + str(average))
        repeat_main()

#DEFINE MAIN FUNCTION
def main():
    option = input(
        'Please type in one of the following numbers and press enter: 1 to perform a calculation, 2 to calculate an average, or 3 to exit. \n')
    while True:
        if option == '1':
            operation = input('Please type in one of the following operations and press enter: + - * / \n')
            perform_calculation(operation)
            break
        elif option == '2':
            calculate_average()
            break
        elif option == '3':
            print('Thank you for using the PyLoops Calculator. Enjoy the rest of your day!')
            sys.exit()
        else:
            option = input(
                'Invalid input. Please try again. \n')
            continue
    repeat_main()

#DEFINE SOURCE FILE AS MAIN PROGRAM
if __name__ == '__main__':
    main()