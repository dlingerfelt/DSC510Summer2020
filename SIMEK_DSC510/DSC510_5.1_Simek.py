def perform_calculation(operation):
    while True:
        if operation == '*' or '/' or '+' or '-':
            break
        else:
            print('Error.  Please enter a valid mathematical operation.')
            continue
    while True:
        try:
            number1 = float(input('Enter the first number: '))
            break
        except ValueError:
            print('Invalid entry.  Please enter the first number.')
            continue
    while True:
        try:
            number2 = float(input('Enter the second number: '))
            break
        except ValueError:
            print('Invalid entry.  Please enter the first number.')
            continue
    if operation == '/' and number2 == 0:
        print('Invalid entry.  Cannot divide by zero.')
    if operation == '*':
        return number1 * number2
    if operation == '/':
        return number1 / number2
    if operation == '+':
        return number1 + number2
    if operation == '-':
        return number1 - number2


def calculate_average():
    quantity = int(input('How many values would you like to average? '))
    q = 0
    sum_num = 0
    while q < quantity:
        number = float(input('Enter a number:  '))
        sum_num = sum_num + number
        q += 1
    return sum_num / quantity


def main():
    while True:
        action = input('What type of operation would you like to perform?\n'
                       '    Enter "1" for mathematical calculation.\n'
                       '    Enter "2" to calculate the average of numbers.\n'
                       '    Enter "3" to terminate the program.\n')
        if action == str('1'):
            operation = input('Please enter the mathematical operation you'
                              ' would like to perform:\n'
                              '    "*" for multiplication\n'
                              '    "/" for division\n'
                              '    "+" for addition\n'
                              '    "-" for subtraction \n')
            print(perform_calculation(operation))
            continue
        if action == str('2'):
            print(calculate_average())
            continue
        if action == str('3'):
            print("Program Complete.")
            break


main()
