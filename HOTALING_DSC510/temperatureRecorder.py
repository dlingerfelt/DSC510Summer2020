# Assignment 6.1
# Michael Hotaling


def temp_recorder():
    temp = []
    while True:
        user_input = input("Please input a temperature: ")
        if user_input.lower() == "quit":
            break
        try:
            temp.append(float(user_input))
        except:
            print("Invalid Entry: Please Try Again!")
    print()
    print("The maximum temperature is " + str(max(temp)))
    print("The minimum temperature is " + str(min(temp)))
    print("The number of measurement inputs is " + str(len(temp)))


if __name__ == "__main__":
    print()
    print("Welcome to the temperature recorder!")
    print("Input a numeric value below.")
    print("Type 'quit' to exit the program")
    temp_recorder()
    again = input("Would you like to run the program again?: ")
    while again.lower()[0] == "y":
        temp_recorder()
        again = input("Would you like to run the program again?: ")
    print("Goodbye!")
