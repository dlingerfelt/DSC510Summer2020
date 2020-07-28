# DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Michael Hotaling
# 07/28/2020


import requests
import time
import webbrowser


def chuck_norris_joke(category):
    try:
        # response = requests.get('https://api.chucknorris.io/jokes/random?category=dev', verify=False)  # My SSL
        # certificates are all messed up so I need to disable verification
        if category == "random":
            api_response = requests.get('http://api.chucknorris.io/jokes/random', verify=False)
        else:
            api_response = requests.get('http://api.chucknorris.io/jokes/random?category=' + category, verify=False)
        json_response = api_response.json()
        return json_response.get('value')
    except requests.HTTPError:
        print("An HTTP Error has occurred. Please try again later.")
        exit()


def category_puller():
    categories = requests.get('http://api.chucknorris.io/jokes/categories', verify=False).json()
    return categories


def joke_selector(categories):
    # This function returns the category of joke the user wants to select.
    # I am literally terrible at using dictionaries, so I decided to use two different lists instead.
    # This is terrible.
    category_numbers = 1
    category_number_list = []
    print("Here are the categories: \nYou can enter either the category name or number: ")
    print("-" * 49)
    for category in list(categories):
        print(" {0:>2} - {1}{2}".format(category_numbers, category.upper()[0], category[1::]))
        category_number_list.append(str(category_numbers))
        category_numbers += 1

    # Random is also a category, but it isn't listed in the list. So let's just add it.
    print(" {0:>2} - {1}".format(category_numbers, "Random"))
    categories.append("random")
    category_number_list.append(str(category_numbers))
    print("-" * 49)
    # print(categories)
    # print(category_number_list)
    while True:
        joke_selection = input("What kind of joke would you like to hear?: ").lower()
        if joke_selection in categories:
            return joke_selection
        elif joke_selection in category_number_list:
            return categories[int(joke_selection)-1]
        else:
            print("Invalid request: Please try again!")


def create_output(joke_list):
    file_name = "Chuck_Norris_Jokes.txt"
    output = open(file_name, "w")
    output.write("Chuck Norris Jokes\n")
    output.write("-" * len("Chuck Norris Jokes") + "\n")
    joke_number = 1
    for joke in joke_list:
        output.write("{:>3}) {}\n".format(joke_number, joke))
        joke_number += 1
    output.close()
    webbrowser.open(file_name)


def main():
    # The main function is a bit long
    print("Welcome to the Chuck Norris Joke Machine")
    categories = category_puller()
    x = 1
    z = 0
    joke_list = []
    while True:
        category = joke_selector(categories)
        while True:
            try:
                y = int(input("How many jokes would you like to hear?: "))
                if y <= 0:
                    print("Please input a positive integer value")
                    continue
                elif y > 99:
                    print("That's too many jokes! \nPlease pick a smaller number!")
                    continue
                z = z + y
                break
                print("Please input a positive integer value")
            except ValueError as error:
                print(str(error) + " :Please enter a positive integer!")

        # This whole block should be it's own function, but I'm finding it hard to return the joke list for output
        print_line = "Pulling {0} {1} joke(s):"
        print("-" * len(print_line.format(y, category)))
        print(print_line.format(y, category))
        print("-" * len(print_line.format(y, category)))
        while x <= z:
            joke = chuck_norris_joke(category)
            print("{:>3}) {}".format(x, joke))
            joke_list.append(joke)
            x += 1
            time.sleep(2)
        print("-" * 40)

        while True:
            user_continue_request = input("Would you like to see more jokes? [y/n]: ").lower()
            if user_continue_request == "y":
                break
            elif user_continue_request == "n":
                if input("Would you like to export your jokes to txt? [y/n]: ").lower() == "y":
                    create_output(joke_list)
                print("Goodbye!")
                exit()
            else:
                print("Invalid request")


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()  # I need this line to run the program on my computer. Very annoying
    main()
