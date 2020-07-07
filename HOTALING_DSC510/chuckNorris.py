# DSC 510
# Week 89
# Programming Assignment Week 9
# Author: Michael Hotaling
# 07/06/2020


import requests
import time
from requests import HTTPError


def chuck_norris_joke():
    try:
        # I'm going to request jokes based on dev humour since some of the jokes not in this category are very explicit
        response = requests.get('https://api.chucknorris.io/jokes/random?category=dev', verify=False)  # My SSL
        # certificates are all messed up so I need to disable verification
        json_response = response.json()
        return json_response.get('value')
    except HTTPError:
        return "An HTTP Error has occurred. Please try again later."


def print_joke(number_of_jokes):
    try:
        joke_counter = int(number_of_jokes)
        for i in range(1, joke_counter + 1):
            # Made some nice formatting
            print(str(i) + ") " + chuck_norris_joke())
            # Added a 1 second wait time to prevent getting blocked by the website
            time.sleep(1)
    except ValueError:
        print("Invalid number. Please try again (or don't.)")


def main():
    print("Welcome to the Chuck Norris Joke Machine: circa 2005....")
    print("Hope you haven't set your expectations too high...")

    try:
        number_of_jokes = int(input("How many bad jokes do you want? (0 is the recommended option:) "))
    except ValueError:
        print("Invalid Entry: Please try again.")
        exit()
    if number_of_jokes < 1:
        print("Good choice")
        exit()
    print("Suit yourself...")
    print()
    print_joke(number_of_jokes)
    print()
    print("You sat through " + str(number_of_jokes) + " Chuck Norris joke(s) ")


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()  # I need this line to run the program on my computer. Very annoying
    main()
