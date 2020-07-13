# Katie Simek
# DSC510-T303
# Assignment 6.1
# 12/7/20
# Ask user for list of temperatures, determine the number of temperatures,
# determine the largest temperature, and the smallest temperature.

# Create an empty list to hold user entered values
temperatures = []

# Loop to ask user for next temperature or end the list
while True:
    value = input('Enter a temperature or "done" to complete the list: ')
    if value == 'done':
        break
    else:
        # Validate user entered values and adds to list, return error
        # if value cannot be converted to a float value
        try:
            temp = float(value)
            temperatures.append(temp)
        except ValueError:
            print('Invalid entry. Enter a temperature or "done" to complete the list.')
            continue

print()
print('The largest temperature is ', max(temperatures), 'degrees')
print('The smallest temperature is ', min(temperatures), 'degrees')
print('The list contains ', len(temperatures), ' temperatures.')
