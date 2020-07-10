# Mike's Stupid Number Machine


# I added the teen numbers to the singles list. This is useful for numbers between 1-19, but if we ever want to increase
# range of this program, we will run into issues. ie 116.
singles_and_teens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                     "twelve",
                     "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# Second digit lists
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# We don't need a hundred list technically. We should be able to check the length of the number. If it is 3, we can pull
# The first digit, index the singles list, and add "hundred" to the string. The rest is self explanatory.

# Testing the program
for i in range(1, 101):
    # len(str(i))
    if i <= 19:
        print(singles_and_teens[i])
    elif 20 <= i <= 99:
        print(str(tens[int(str(i)[0]) - 2]) + " " + str(singles_and_teens[int(str(i)[1])]))
    else:
        print("Didn't program that in yet!")
