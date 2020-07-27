#DSC 510

#Week 6

#Programming Assignment Week 6

#Author Tiffany Tesoro

#07/12/2020

print()

#USER_INPUT FUNCTION DEFINITION
def user_input(temperatures):
    while True:
        try:
            temp_input = input(
                'Type in a temperature excluding the unit degrees F/C then press enter or type DONE when all desired values are entered. \n')
            temperatures.append(float(temp_input))
        except ValueError:
            if temp_input == 'DONE':
                break
            else:
                print("Please try again and input numerical digits.")
    print()
    print('--- RESULTS ---')
    print('The largest temperature is ' + str(max(temperatures)))
    print('The smallest temperature is ' + str(min(temperatures)))
    print('There are ' + str(len(temperatures)) + ' temperature readings in the list.')
    print(sorted(temperatures))

#MAIN FUNCTION
def main():
    print('--- Welcome! The purpose of this program is to identify high and low temperature readings. ---')
    while True:
        temperatures = []
        print()
        temperatures = user_input(temperatures)
        print()
        redo = input('Type REDO to input a new set of temperatures then press enter or type DONE to end program. \n')
        if redo == 'REDO':
            continue
        elif redo == 'DONE':
            print('Program ending. Have a great rest of your day!')
            break
        else:
            print("Please try again.")

if __name__ == "__main__":
    main()