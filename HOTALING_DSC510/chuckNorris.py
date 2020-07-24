# DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Michael Hotaling
# 07/06/2020


import requests


def chuck_norris_joke(category):
    try:
        # response = requests.get('https://api.chucknorris.io/jokes/random?category=dev', verify=False)  # My SSL
        # certificates are all messed up so I need to disable verification
        if category == "random":
            api_response = requests.get('https://api.chucknorris.io/jokes/random', verify=False)
        else:
            api_response = requests.get('https://api.chucknorris.io/jokes/random?category=' + category, verify=False)
        json_response = api_response.json()
        return json_response.get('value')
    except requests.HTTPError:
        return "An HTTP Error has occurred. Please try again later."


def joke_selector():
    # This function returns the category of joke the user wants to select.
    # I am literally terrible at using dictionaries, so I decided to use two different lists instead.
    # This is terrible.
    categories = requests.get('https://api.chucknorris.io/jokes/categories', verify=False).json()
    category_numbers = 1
    category_number_list = []
    print("Here are the categories:")
    print("-" * 24)
    for category in list(categories):
        print("{0:>2}) {1}{2}".format(category_numbers, category.upper()[0], category[1::]))
        category_number_list.append(str(category_numbers))
        category_numbers += 1
    print("{0:>2}) {1}".format(category_numbers, "Random"))
    categories.append("random")
    category_number_list.append(str(category_numbers))
    print("-" * 24)
    # print(categories)
    # print(category_number_list)
    while True:
        joke_selection = input("What kind of joke would you like to hear?: ")
        if joke_selection.lower() in categories:
            return joke_selection.lower()
        elif joke_selection in category_number_list:
            return categories[int(joke_selection)-1]
        else:
            print("Invalid request: Please try again!")


def main():
    print("Welcome to the Chuck Norris Joke Machine")
    x = 1
    z = 0
    while True:
        category = joke_selector()
        while True:
            try:
                y = int(input("How many jokes would you like to hear?: "))
                z = z + y
                break
            except ValueError as error:
                print(error)
                print("Please input a positive integer value")

        print("-"*40)
        while x <= z:
            print("{:>3}) {}".format(x, chuck_norris_joke(category)))
            x += 1
        print("-" * 40)
        if input("Would you like to see more jokes? [y/n]: ").lower() == "y":
            continue
        else:
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()  # I need this line to run the program on my computer. Very annoying
    main()
