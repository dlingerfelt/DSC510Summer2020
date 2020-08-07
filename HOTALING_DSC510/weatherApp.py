# DSC 510
# Week 10
# Programming Assignment Week 10: Final Project
# Author: Michael Hotaling
# 08/06/2020


import requests
import datetime
import configparser
from requests.exceptions import HTTPError


# Class to represent config values (api_key, units, country, language, base URl)
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


# Function to request weather data from the API
def get_weather_data(query, config):
    complete_url = "{}{}&appid={}".format(config.base_url, query, config.api_key)
    response = requests.get(complete_url)
    # try-except block
    try:
        # get the API value into response
        # print(complete_url)
        response.raise_for_status()
        if response.status_code == 200:
            print("API Request Successful")
        return response.json()
    # Exception Handling
    except HTTPError:
        print("Response status code: " + str(response.status_code))
        if response.status_code == 400:
            print("Syntax Error!")
        # if status code 404 is received from the API
        elif response.status_code == 404:
            print("Unable to find location: Please try again")
        # if status code 401 is received from the API
        elif response.status_code == 401:
            print("Invalid API Key. Please update your API key.")
        elif response.status_code == 429:
            print("Your account is temporary blocked due to exceeding of requests limitation of your subscription type")
        else:
            print("An unknown error has occurred. Please try again later!")


# Function to display results from JSON
def display_results(weather, weather_data):
    # try-except block
    # Looping the weather list of JSON objects to print the weather details for the selected range
    header_block = "| {0:<21} | {1:>8} | {2:>11} | {3:>8} | {4:>8} | {5:>8} |  {6:>9} | {7:<15} | {8:<25} |" \
                   " {9:>10} | {10:>15} |   {11:>15} |" \
        .format('Local Time',
                'Temp',
                'Feels Like',
                'Temp Min',
                'Temp Max',
                'Pressure',
                'Humidity',
                'Weather',
                'Description',
                'Wind Speed',
                'Wind Direction',
                'Cloud Coverage')
    # Current Weather Details
    if weather_data == "1":
        print()
        time_at_location = weather['dt']
        time_zone_at_location = weather['timezone']
        time_at_location += time_zone_at_location
        print('-' * 36)
        print("| Location   : {:<19} |".format((weather['name'] + ", " + (weather['sys']['country']))))
        print("| Local Time : {:<19} |".format(str(datetime.datetime.utcfromtimestamp(time_at_location))))
        print("| Sunrise    : {:<19} |".format(str(datetime.datetime.utcfromtimestamp(weather['sys']['sunrise'] +
                                                                                      time_zone_at_location))))
        print("| Sunset     : {:<19} |".format(str(datetime.datetime.utcfromtimestamp(weather['sys']['sunset'] +
                                                                                      time_zone_at_location))))
        print("| Query      : {:<19} |".format(str("Current Weather")))
        print("-" * len(header_block))
        print(header_block)
        print("-" * len(header_block))
        print(
            "| {0:<21} | {1:>8.2f} | {2:>11.2f} | {3:>8.2f} | {4:>8.2f} | {5:>8} | {6:>9}% | {7:<15} | {8:<25} |"
            " {9:>10.2f} | {10:>15} |  {11:>15}% |".format(str(
                datetime.datetime.utcfromtimestamp(time_at_location)),
                weather['main']['temp'],
                weather['main']['feels_like'],
                weather["main"]["temp_min"],
                weather["main"]["temp_max"],
                weather['main']['pressure'],
                weather['main']['humidity'],
                weather['weather'][0]['main'],
                weather['weather'][0]['description'],
                weather['wind']['speed'],
                weather['wind']['deg'],
                weather['clouds']['all']))
        print("-" * len(header_block))

    # Forecast Weather Details
    elif weather_data == "2":
        timezone = weather['city']['timezone']
        print()
        local_time = datetime.datetime.utcfromtimestamp(
            round(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).timestamp() + timezone, 0))
        print('-' * 36)
        print("| Location   : {:<19} |".format((weather['city']['name']) + ", " + (weather['city']['country'])))
        print("| Local Time : {:<19} |".format(str(local_time)))
        print("| Sunrise    : {:<19} |".format(str(datetime.datetime.utcfromtimestamp(weather['city']['sunrise'] +
                                                                                      timezone))))
        print("| Sunset     : {:<19} |".format(str(datetime.datetime.utcfromtimestamp(weather['city']['sunset'] +
                                                                                      timezone))))
        print("| Query      : {:<19} |".format(str("Weather Forecast")))
        print("-" * len(header_block))
        print(header_block)
        print("-" * len(header_block))
        # Iteratively go through the list that the JSON provides
        for i in weather['list']:
            print(
                "| {0:<21} | {1:>8.2f} | {2:>11.2f} | {3:>8.2f} | {4:>8.2f} | {5:>8} | {6:>9}% | {7:<15} |"
                " {8:<25} | {9:>10.2f} | {10:>15} |  {11:>15}% |".format(
                    str(datetime.datetime.utcfromtimestamp(i["dt"] + timezone)),  # 0
                    i["main"]["temp"],  # 1
                    i['main']['feels_like'],  # 2
                    i["main"]["temp_min"],  # 3
                    i["main"]["temp_max"],  # 4
                    i['main']['pressure'],  # 5
                    i['main']['humidity'],  # 6
                    i['weather'][0]['main'],  # 7
                    i['weather'][0]['description'],  # 8
                    i['wind']['speed'],  # 9
                    i['wind']['deg'],  # 10
                    i['clouds']['all']))  # 11
        print("-" * len(header_block))


def config_editor(make_change):
    config = get_config()
    api_key = config.api_key
    language = config.language
    country = config.country
    units = config.units
    if make_change == "1":
        temp_setting = input("Please select either F, C, or K: ")
        if temp_setting.lower() == "f":
            units = "imperial"
        elif temp_setting.lower() == "c":
            units = "metric"
        elif temp_setting.lower() == "k":
            units = 'kelvin'
        else:
            print("Invalid Entry")

    elif make_change == "2":
        new_country = input("Please select a country using a two character country code: ").upper()
        # This is probably a dumb way to do this, but oh well!
        if new_country not in ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ',
                               'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV',
                               'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN',
                               'CX', 'CC', 'CO', 'KM', 'CD', 'CG', 'CK', 'CR', 'HR', 'CU', 'CW', 'CY', 'CZ', 'CI', 'DK',
                               'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI',
                               'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU',
                               'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR',
                               'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW',
                               'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV',
                               'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA',
                               'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO',
                               'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'MK',
                               'RO', 'RU', 'RW', 'RE', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA',
                               'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK',
                               'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT',
                               'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'US', 'UY', 'UZ', 'VU', 'VE',
                               'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'AX']:
            print("Country not found!")
        else:
            country = new_country

    elif make_change == "3":
        # https://openweathermap.org/current#multi
        language = input("The full list of languages can be found here:\nhttps://openweathermap.org/current#multi "
                         "\nPlease select a language: ").upper()

    elif make_change == "4":
        api_key_new = input("Please enter a new API key: ")
        complete_url = "{}weather?zip={},{}&appid={}".format(config.base_url, "11210", "US", api_key_new)
        response = requests.get(complete_url)
        try:
            response.raise_for_status()
            if response.status_code == 200:
                print("Successfully connected to the API")
                api_key = api_key_new
        except HTTPError:
            if response.status_code == 401:
                print("Invalid API key. Please try again!")
            else:
                print("Another error has occurred")
    else:
        pass
    if language == config.language \
            and country == config.country \
            and units == config.units \
            and api_key == config.api_key:
        print("No Changes Made!")
    else:
        config_file = open("config.ini", "w")
        config_file.write("[openweathermap]\n")
        config_file.write("api_key={}\n".format(api_key))
        config_file.write("units={}\n".format(units))
        config_file.write("country={}\n".format(country))
        config_file.write("language={}\n".format(language))
        config_file.write("base_url=http://api.openweathermap.org/data/2.5/")
        config_file.close()
        print("Configuration Saved!")


def main():
    # Fetching User Parameters from Config File.
    config = get_config()
    units = config.units
    country = config.country
    language = config.language
    api_key = config.api_key
    counter = 1
    now = datetime.datetime.now()
    print()
    print("Welcome to the Weather App")
    print("Today is {0}".format(now.strftime("%A, %B %d, %Y")))
    print("The Time is currently {0}".format(now.strftime("%I:%M%p")))
    print("-" * 30)
    while True:
        print()
        user_selection = input("Main Menu:\n "
                               "1: Pull the current weather for a city or ZIP code\n "
                               "2: Pull forecast data for a city or ZIP code\n "
                               "3: Edit configuration\n "
                               "4: Exit\n"
                               "Please input a selection: ")
        if user_selection in ["1", "2"]:
            if user_selection == "1":
                weather_option = "weather"
            else:
                while True:
                    try:
                        counter = int(input("How much data would you like to pull? [3hr blocks/40 max]: "))
                        if 1 <= counter <= 40:
                            break
                        else:
                            print("Please enter a number between 1 and 40 ")
                    except ValueError:
                        print("Please input an integer value!")
                weather_option = "forecast"
            location = input("Please input a city name or ZIP code: ")

            if location.isdigit() and len(location) == 5:  # If it is a ZIP code
                print("ZIP code detected")
                query = "{}?zip={},{}&units={}&lang={}&cnt={}" \
                    .format(weather_option, location, country, units, language, counter)

            else:  # If it is a city name
                query = "{}?q={},{}&units={}&lang={}&cnt={}" \
                    .format(weather_option, location, country, units, language, counter)
            weather_data = get_weather_data(query, config)
            if not weather_data:
                # If nothing is returned due to an invalid request, we will just exit back to
                # the main program since the error handling is done in the function
                pass
            else:
                display_results(weather_data, str(user_selection))

        elif user_selection == "3":
            print()
            make_change = input("Configuration: \n 1: units: {0} \n 2: country: {1}\n 3: language: "
                                "{2}\n 4: API Key: {3}\n Please select the config you wish to change: "
                                .format(units, country, language, api_key))
            config_editor(make_change)
            config = get_config()
            units = config.units
            country = config.country
            language = config.language
            api_key = config.api_key

        elif user_selection == "4":
            print("Thank you for using the Weather App!")
            print("Goodbye")
            exit()
        else:
            print("Invalid Request: Please try again")


if __name__ == '__main__':
    main()
