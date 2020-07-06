# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Michael Hotaling
# 07/06/2020


def median(numbers):
    # Added this for fun
    # This function will find the median value in a list
    # We will first sort the list from lowest to highest and find the length of the list
    # If the list length is even, we will need to use floor division to find the two middle values and average them
    # If the list is odd, we just need to pull the middle value
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        med1 = numbers[length // 2]
        med2 = numbers[length // 2 - 1]
        med = (med1 + med2) / 2
        return med
    else:
        med = numbers[(length // 2)]
        return med


def temp_recorder(temp):
    # This function records the entries from the user by appending an empty list.
    # The escape argument, also known as the sentinel value, will be the string "quit"
    # There is error handling just in case the user inputs an invalid data type like a string or boolean
    while True:
        # This while loop will continuously ask for inputs until the user inputs "quit"
        # quit can be in any format since we check to see if the lower case values are equal to the sentinel string
        user_input = input("Please input temperature number " + str(len(temp) + 1) + ": ")
        if user_input.lower() == "quit":
            return temp
        # This is error handling just in case the user tries to input an invalid data type. Since this is a while
        # loop, the user has the opportunity to try and input another value without the program crashing
        try:
            temp.append(float(user_input))
        except ValueError:
            print("Invalid entry: Please try again!")

    # Here we will print out the results of the list.
    # If the list is empty, or something else went wrong, it will print the except statement.


def pretty_format(temp_list):
    try:
        print()
        print("The list of temperatures is [" + ', '.join(map(str, temp_list)) + "]")
        print("The maximum temperature is " + str(max(temp_list)))
        print("The minimum temperature is " + str(min(temp_list)))
        print("The number of measurement inputs is " + str(len(temp_list)))
        print("The average value of measurement inputs is " + str(sum(temp_list) / len(temp_list)))
        print("The median value of the measurement inputs is " + str(median(temp_list)))

    except ValueError:
        print("Something went wrong!")
        print("Did you forget to input a temperature? ")
        print("Please try again!")


def main():
    # We will greet the user and print the instructions on how to use the program
    temps = []
    print()
    print("Welcome to the temperature recorder!")
    print("Input a numeric value below.")
    print("Type 'quit' to exit the program")
    # We will use a while loop to ask the user if they want to run the program again
    # We also added a neat little feature by asking the user if they want to continue where they left off
    # That way, they don't have to worry about accidentally inputting the sentinel value and losing their data
    while True:
        print()
        temps = temp_recorder(temps)
        pretty_format(temps)
        print()
        again = input("Would you like to run the program again? [y/n]:  ")
        if again.lower()[0] != "y":
            break
        # Here, we give the user the opportunity to either continue with their list, or start fresh.
        user_continue = input("Would you like to continue where you left off? [y/n]: ")
        if user_continue.lower()[0] != "y":
            # This line resets the temp values
            temps = []
            print("List erased! Starting over!")
    print("Goodbye!")
    exit()


# Here, we will call the program with the __main__ statement.
if __name__ == "__main__":
    main()
