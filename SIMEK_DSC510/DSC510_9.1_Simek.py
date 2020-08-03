# Katie Simek
# 02/08/2020
# Create a program that uses the Request library to make a GET request of
# the specified API.  Parse and format the response to print the
# "value" key to the user.  Allow the program to be repeated until the user
# terminates the program.


import requests
import textwrap


def main():
    # Welcome greeting
    print('Hello,')
    # Evaluate if they would like initial joke, loop to validate user input
    while True:
        action = input('Would you like a Chuck Norris joke?\n'
                       'Enter "Yes" or "No"\n')
        # Converting sting input to lowercase for validation
        action = action.lower()
        if action == str('yes'):
            # Use the Request library to GET joke from API link
            response = requests.get('https://api.chucknorris.io/jokes/random')
            # Assigning Response to variable and converting to JSON
            joke = response.json()
            print()   # Blank line
            # Formatting Joke response to limit line length
            print(textwrap.fill(joke["value"]))
            print()   # Blank line
            # After first joke, asking if the user would like another joke,
            # loops until user terminates the program
            while True:
                action2 = input('Would you like another Chuck Norris joke?\n'
                                'Enter "Yes" or "No".\n')
                # Converting sting input to lowercase for validation
                action2 = action2.lower()
                if action2 == str('yes'):
                    # Use the Request library to GET joke from API link
                    response = requests.get('https://api.chucknorris.io/jokes/random')
                    # Assigning Response to variable and converting to JSON
                    joke = response.json()
                    print()  # Blank line
                    # Formatting Joke response to limit line length
                    print(textwrap.fill(joke["value"]))
                    print()  # Blank line
                    continue
                # Response for if user says no to another joke after the first
                if action2 == str('no'):
                    print('Okay, no more jokes for you. Goodbye.')
                    quit()
                # Return error for invalid entry to question for another joke
                else:
                    print('**** Invalid entry. ****\n'
                          'Please enter "Yes" or "No".\n')
                    continue
        # Response for if user says no to first joke
        if action == str('no'):
            print('Okay, no joke for you.  Goodbye.')
            quit()
        # Return error for invalid entry to initial question
        else:
            print('**** Invalid entry. ****\n'
                  'Please enter "Yes" or "No".\n')
            continue


if __name__ == "__main__":
    main()


