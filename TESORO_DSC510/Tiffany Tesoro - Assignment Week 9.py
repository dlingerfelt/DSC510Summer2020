#DSC 510

#Week 9

#Programming Assignment Week 9

#Author Tiffany Tesoro

#08/02/2020

#TO USE API TO GET DATA
import json
import requests
#^^ had some trouble using this until i figured out how to install pip via terminal on my mac

#DEFINE JOKE_REQUEST FUNCTION
def joke_request():
    while True:
        hearajoke = input('Would you like to hear a joke? Type Y or N then press enter.\n')
        if(hearajoke == 'Y' or hearajoke == 'y'):
            #CALL TO CNJOKES FUNCTION
            cn_jokes()
        elif(hearajoke == 'N' or hearajoke == 'n'):
            print('Program will now end. Thank you for using the Random Chuck Norris Jokes Generator!')
            exit()
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
        #REFERENCE FOR 'OR' USAGE IN 'IF' STATEMENT - https://www.datacamp.com/community/tutorials/python-if-elif-else

#DEFINE CNJOKES FUNCTION
def cn_jokes():
    #REFERENCE FOR EXTRACTING DATA FROM API - https://python.gotrained.com/python-json-api-tutorial/
    #Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
    response = requests.get('https://api.chucknorris.io/jokes/random')
    #The program will receive a JSON response which includes various pieces of data.
    data = response.text
    #You should parse the JSON data to obtain the “value” key.
    parsed = json.loads(data)
    value = parsed['value']
    #chose value because that is where the joke is listed under in the api
    #PRETTY PRINT FORMAT?
    print()
    print('Here\'s a joke for you...')
    #The data associated with the value key should be displayed for the user (i.e., the joke).
    print(value)
    print()
    print()
    #CALL TO JOKE_AGAIN FUNCTION
    joke_again()

#DEFINE JOKE_AGAIN FUNCTION
#Your program should allow the user to request a Chuck Norris joke as many times as they would like.
def joke_again():
    while True:
        anotherjoke = input('Would you like to hear another joke? Type Y or N then press enter.\n')
        if(anotherjoke == 'Y' or anotherjoke == 'y'):
            cn_jokes()
        elif(anotherjoke == 'N' or anotherjoke == 'n'):
            print('Program will now end. Thank you for using the Random Chuck Norris Jokes Generator!')
            exit()
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue

#DEFINE MAIN FUNCTION
def main():
    #WELCOME MESSAGE
    print()
    print('Welcome to the Random Chuck Norris Jokes Generator!')
    #CALL TO JOKE_REQUEST FUNCTION
    joke_request()

#CALL TO MAIN FUNCTION
if __name__ == "__main__":
    main()