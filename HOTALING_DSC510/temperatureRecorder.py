# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Michael Hotaling
# 06/15/2020

def median(numbers):
    # This function will find the median value in a list
    # We will first sort the list from lowest to highest and find the length of the list
    # If the list length is even, we will need to use floor division to find the two middle values and average them
    # If the list is odd, we just need to pull the middle value
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        median1 = numbers[length//2]
        median2 = numbers[length//2 - 1]
        median = (median1 + median2)/2
        return(median)
    else:
        median = numbers[int(length/2)]
        return (median)

def temp_recorder():
    # This function records the entries from the user by appending an empty list.
    # The escape argument, also known as the sentinel value, will be the string "quit"
    # There is error handling just in case the user inputs an invalid data type like a string or boolean
    temp = []
    while True:
        # This while loop will continuously ask for inputs until the user inputs "quit"
        # quit can be in any format since we check to see if the lower case values are equal to the sentinel string
        user_input = input("Please input a temperature: ")
        if user_input.lower() == "quit":
            break
        # This is error handling just in case the user tries to input an invalid data type
        try:
            temp.append(float(user_input))
        except:
            print("Invalid Entry: Please Try Again!")
    print()
    # Here we will print out the results of the list.
    # If the list is empty, or something else went wrong, it will print the except statement.
    try:
        print("The maximum temperature is " + str(max(temp)))
        print("The minimum temperature is " + str(min(temp)))
        print("The number of measurement inputs is " + str(len(temp)))
        print("The average value of measurement inputs is " + str(sum(temp)/len(temp)))
        print("The median value of the measurement inputs is "+ str((median(temp))))

    except:
        print("Something went wrong!")
        print("Did you forget to input a temperature? ")
        print("Please try again!")



# Here, we will call the program with the __main__ statement.
# We will greet the user and print the instructions on how to use the program
if __name__ == "__main__":
    print()
    print("Welcome to the temperature recorder!")
    print("Input a numeric value below.")
    print("Type 'quit' to exit the program")
    temp_recorder()

    # I wanted the program to recursively ask the user if they want to run the program again, but I can't figure out
    # a good way to do that. This is what I came up with
    again = input("Would you like to run the program again?: ")
    while again.lower()[0] == "y":
        temp_recorder()
        again = input("Would you like to run the program again?: ")
    print("Goodbye!")
