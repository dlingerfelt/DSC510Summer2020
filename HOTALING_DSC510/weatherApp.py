# DSC 510
# Week 10
# Programming Assignment Week 10: Final Project
# Author: Michael Hotaling
# 07/28/2020


import requests
import datetime
import configparser
from requests.exceptions import HTTPError


# Class to represent config values ( api_key, units, country, language, base URl )
class Config:
    def __init__(self, api_key, units, country, language, base_url):
        self.api_key = api_key
        self.units = units
        self.country = country
        self.language = language
        self.base_url = base_url


# Function to retrieve configuration values from config file
def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return Config(config['openweathermap']['api_key'],
                  config['openweathermap']['units'],
                  config['openweathermap']['country'],
                  config['openweathermap']['language'],
                  config['openweathermap']['base_url'])


# function to request for weather data
def get_weather_data(query, config):
    # try-except block
    try:
        api_key = config.api_key
        base_url = config.base_url
        complete_url = "{}{}&appid={}".format(base_url, query, api_key)
        # print(complete_url)
        # get the API value into response
        response = requests.get(complete_url)

        # This returns an HTTPError if an error occurred during the retrieval process
        response.raise_for_status()
        # if status code 200 is successfully received the data from API
        if response.status_code != 200:
            print(HTTPError)
        # convert response details into json response as JSON format
        return response.json()
    # Exception Handling
    except HTTPError as http_err:
        print(f'An HTTP error has occurred: {http_err}')
    except Exception as err:
        print(f'Another error has occurred: {err}')


# function to display results from Json
def display_results(weathers, weather_data):
    # try-except block
    try:
        # Looping the weathers list of JSON objects to print the weather details for the selected Range
        if weather_data == "2":
            print("Location : " + (weathers['city']['name']))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
            print("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                  .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description', 'Wind Speed',
                          'Wind Direction'))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
            for i in weathers['list']:
                print(
                    "| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                        .format(i["dt_txt"], i["main"]["temp"], i["main"]["temp_min"], i["main"]["temp_max"],
                                i['main']['pressure'], i['main']['humidity'], i['weather'][0]['description'],
                                i['wind']['speed'], i['wind']['deg']))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
        # Current Weather details
        elif weather_data == "1":
            print("Location : " + (weathers['name']))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
            print("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                  .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description', 'Wind Speed',
                          'Wind Direction'))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
            print(
                "| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                    .format(str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")),
                            weathers['main']['temp'],
                            weathers["main"]["temp_min"],
                            weathers["main"]["temp_max"],
                            weathers['main']['pressure'],
                            weathers['main']['humidity'],
                            weathers['weather'][0]['description'],
                            weathers['wind']['speed'],
                            weathers['wind']['deg']))
            print("-" * len("| {:<21} | {:>8} | {:>8} | {:>8} | {:>8} | {:>9} | {:<25} | {:>10} | {:>15} |"
                            .format('Date', 'Temp', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Description',
                                    'Wind Speed', 'Wind Direction')))
        else:
            print("Invalid Entry")
    except HTTPError:
        print("Unable to get weather information for the input city/zip-code. Please try again!")


def main():
    try:
        # Fetching Default Parameter Country as US and Units - Imperial from configuration file
        config = get_config()
        units = config.units
        country = config.country
        language = config.language
        counter = 1
        now = datetime.datetime.now()
        print("Welcome to the Weather App")
        print("Today is {0}".format(now.strftime("%A, %B %d, %Y")))
        print("The Time is currently {0}".format(now.strftime("%I:%M%p")))
        print("-" * 30)
        while True:
            user_selection = input("Please select an option:\n "
                                   "1: Pull the current weather for a city or ZIP code\n "
                                   "2: Pull forecast data for a city or ZIP code\n "
                                   "3: Edit Configuration\n "
                                   "4: Exit\n")
            if user_selection in ["1", "2"]:
                if user_selection == "1":
                    weather_option = "weather"
                else:
                    counter = input("How much data would you like to pull? [3hr blocks]: ")
                    weather_option = "forecast"
                location = input("Please input a city name or ZIP code: ")

                if location.isdigit(): # If it is a ZIP code
                    # TODO // Gotta make this cleaner
                    query = weather_option + '?zip=' + location + "," + country + "&" + "units=" + units + "&" + "lang=" + language + "&cnt=" + str(
                        counter)
                else:
                    query = weather_option + '?q=' + location + "," + country + "&" + "units=" + units + "&" + "lang=" + language + "&cnt=" + str(
                        counter)
                weather_data = get_weather_data(query, config)
                display_results(weather_data, str(user_selection))

            elif user_selection == "3":
                # Open and edit the config file
                print("Oops! Not available yet!")

            elif user_selection == "4":
                print("Goodbye!")
                exit()

            else:
                print("Invalid Request: Please try again")

    except ValueError or HTTPError:
        print("oops")


if __name__ == '__main__':
    main()
