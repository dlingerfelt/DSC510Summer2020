import time

# Defines possible operations and the associated names of those operations
operatorArray = ['+', '-', '*', '/', '^', '%']
operatorNames = ['Add', 'Subtract', 'Multiply', 'Divide', 'Exponential', 'Remainder']

# Combines the arrays in a new array for visual representation in the performCalculation function
bothOperators = [operatorArray, operatorNames]

# Defines the add function to find the sum of user numbers num1 & num2
def add(a, b):
    return a + b

# Defines the subtract function to find the difference of user numbers num1 & num2
def subtract(a, b):
    return a - b

# Defines the multiply function to find the product of user numbers num1 & num2
def multiply(a, b):
    return a * b

# Defines the divide function to find the quotient of user numbers num1 & num2
def divide(a, b):
    return a / b

# Defines the exponent function to find the power of user numbers num1 & num2
def exponent(a, b):
    return a ** b

# Defines the remainder function to find the remainder after dividing user numbers num1 by num2
def remainder(a, b):
    return a % b

# The operation function takes user numbers num1 & num2 and returns the users appropriate result   
def operation(a, b):
    operator = performCalculation.operator
    if operator == '+':
        print('The ADDITION of ' + str(num1) + ' plus ' + str(num2) + ' is equal to: ' + str(add(a, b)))
    if operator == '-':
        print('The SUBTRACTION of ' + str(num1) + ' minus ' + str(num2) + ' is equal to: ' + str(subtract(a, b)))
    if operator == '*':
        print('The PRODUCT of ' + str(num1) + ' multiplied by ' + str(num2) + ' is equal to: ' + str(multiply(a, b)))
    if operator == '/':
        print('The QUOTIENT of ' + str(num1) + ' divided by ' + str(num2) + ' is equal to: ' + str(divide(a, b)))
    if operator == '^':
        print('The RESULT of ' + str(num1) + ' to the power of ' + str(num2) + ' is equal to: ' + str(exponent(a, b)))
    if operator == '%':
        print('The REMAINDER of ' + str(num1) + ' divided by ' + str(num2) + ' is equal to: ' + str(remainder(a, b)))
 
# restart function cancels or continues the performCalculation function at the users request
def restart():
    runAgain = input("Would you like to run the calculator again? (y/n)" + "\n")

# Restarts program 
    if runAgain == 'y':
        performCalculation()

# Ends program
    elif runAgain == 'n':
        print("Thank you for using Foster Instruments Calculator!")
        return False
    else:
        print("Invalid entry, please try again")
            
# Initiate classes for possible errors in the program
class Error(Exception):
    pass
class NotNumberError(Error):
    pass

# The main function that initiates all other necessary functions
# Receives user input and directs programs based on input
def performCalculation():
    while True:
        
        global num1
        global num2
        
        print('\n' + 'The following list are the options to choose from:')
        
        # Lists possible operations for user to choose from
        for i in zip(*bothOperators):
            print(*i)
        
        # Provides details how to initiate the calculateAverage function
        print("\n" + "Or type 'average' if you would like to get the average from a list of numbers.")
        
        # Receives user input on their operator of choice
        time.sleep(1)
        performCalculation.operator = input("Enter operation choice here, or enter done to exit." + "\n")
            
        operator = performCalculation.operator
        
        # if/elif/else statement to receive the users numbers of choice
        if operator == '' or operator.lower() == 'done':
            break
        
        # Retrieves input numbers from user
        elif operator in operatorArray or operator in operatorNames:
            while True:
                try:
                    num1 = float(input("Enter the first number to use: "))
                except ValueError:
                    print("Not a number, try again.")
                    continue
                else:
                    break
                
            while True:
                try:
                    num2 = float(input("Enter the second number to use: "))
                except ValueError:
                    print("Not a number, try again.")
                    continue
                else:
                    break
            
            # Calls the operation() function based on user input
            operation(float(num1), float(num2))
            
            # Calls the restart() function and continues or cancels program based on user choice
            restart()
            
            break
        
        # Calls calculateAverage if user so choices
        elif operator.lower() == 'average':
            questionAverage()
            break
        
        # Error handling                 
        else: 
            print("Invalid entry, please try again.")
            performCalculation()

# Empty array the user will eventually provide elements for
numbersList = []            

# Function to initiate the average calculation if numberList is adequate for user  
def calculateAverage():
    sum = 0
    global numbersList
    global number
    
    while True:
        global number
        
        # Input from user if average list is acceptable
        averageAnswer = input('Does the following list look correct for the totaling and averaging?' + '\n\n' + str(numbersList)[1:-1] + 
                              '\n' + 'Please answer y for yes or n for no:' + '\n')
        
        # If numbersList is correct, provides the average of the numbers in the list
        if averageAnswer == 'y':
            for nums in numbersList:
                sum = sum + nums
                
            # Calculates Average of numbersList
            numbersAverage = sum / len(numbersList)
            print('The sum of your list is: ' + str(sum))
            time.sleep(0.5)
            print('The average of your list is: ' + str(numbersAverage))
            restart()
            break
        
        elif averageAnswer == 'n':
            print('Please re-enter your list:')
            for i in range(0, number):
                questionAverage()
        else:
            print('Invalid entry, please try again.')

# Initiates user input on how many numbers to average, and which numbers to average            
def questionAverage():
    while True:
        try:
            number = int(input('How many numbers would you like to get the average of?' + '\n'))
        
        # Error if user does not input an integer21231197
        except ValueError:
            print("Not a number, try again.")
            continue        
        
        print('Please enter each number you would like in your list to average:')
        
        # Beginning of numbers in array, numbersList
        for i in range(0, number):
            try:
                numbersToAverage = float(input('Number ' + str(i + 1) + ' is: '))
            except ValueError:
                print('Not a number, please try again')
                continue
            
            numbersList.append(numbersToAverage)
    
        calculateAverage()
        
        return False