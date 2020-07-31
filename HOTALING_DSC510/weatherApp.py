# DSC 510
# Week 10
# Programming Assignment Week 10: Final Project
# Author: Michael Hotaling
# 07/31/2020


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
        # TODO // Enable this back eventually
        # response.raise_for_status()

        # if status code 200 is successfully received the data from API
        print("Response status code:" + str(response.status_code))
        if response.status_code == 200:
            print("API Request Successful")
            return response.json()
        elif response.status_code == 400:
            print("Syntax Error!")
        # if status code 404 is received from the API
        elif response.status_code == 404:
            print("Unable to find location: Please try again")
        # if status code 401 is received from the API
        elif response.status_code == 401:
            print("Invalid API Key. Please update your API key.")
        elif response.status_code == 429:
            print("Your account is temporary blocked due to exceeding of requests limitation of your subscription type")
        # convert response details into json response as JSON format

    # Exception Handling
    except HTTPError as httperror:
        print(httperror)
    except Exception as error:
        print(error)


# function to display results from Json
def display_results(weathers, weather_data):
    # try-except block
    try:
        # Looping the weathers list of JSON objects to print the weather details for the selected range
        header_block = "| {0:<21} | {1:>8} | {2:>11} | {3:>8} | {4:>8} | {5:>8} |  {6:>9} | {7:<15} | {8:<25} |" \
                       " {9:>10} | {10:>15} |   {11:>15} |" \
            .format('Date', 'Temp', 'Feels Like', 'Temp Min', 'Temp Max', 'Pressure', 'Humidity', 'Weather',
                    'Description', 'Wind Speed', 'Wind Direction', 'Cloud Coverage')

        if weather_data == "2":
            print("Location : " + (weathers['city']['name']) + ", " + (weathers['city']['country']))
            print("-" * len(header_block))
            print(header_block)
            print("-" * len(header_block))
            for i in weathers['list']:
                print(
                    "| {0:<21} | {1:>8.2f} | {2:>11.2f} | {3:>8.2f} | {4:>8.2f} | {5:>8} | {6:>9}% | {7:<15} |"
                    " {8:<25} | {9:>10.2f} | {10:>15} |  {11:>15}% |".format(
                                i["dt_txt"],  # 0
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
        # Current Weather details
        elif weather_data == "1":
            print("Location : " + (weathers['name']) + ", " + (weathers['sys']['country']))
            print("-" * len(header_block))
            print(header_block)
            print("-" * len(header_block))
            print(
                "| {0:<21} | {1:>8.2f} | {2:>11.2f} | {3:>8.2f} | {4:>8.2f} | {5:>8} | {6:>9}% | {7:<15} | {8:<25} |"
                " {9:>10.2f} | {10:>15} |  {11:>15}% |".format(str(
                            datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")),
                            weathers['main']['temp'],
                            weathers['main']['feels_like'],
                            weathers["main"]["temp_min"],
                            weathers["main"]["temp_max"],
                            weathers['main']['pressure'],
                            weathers['main']['humidity'],
                            weathers['weather'][0]['main'],
                            weathers['weather'][0]['description'],
                            weathers['wind']['speed'],
                            weathers['wind']['deg'],
                            weathers['clouds']['all']))
            print("-" * len(header_block))
        else:
            print("Invalid Entry")
    except HTTPError:
        print("Unable to get weather information for the input city/zip-code. Please try again!")
    except:
        print("Please try again!")


def main():
    # try-except block
    try:
        # Fetching Default Parameter Country as US and Units - Imperial from configuration file
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
                    counter = input("How much data would you like to pull? [3hr blocks]: ")
                    weather_option = "forecast"
                location = input("Please input a city name or ZIP code: ")

                if location.isdigit() and len(location) == 5:  # If it is a ZIP code
                    query = "{}?zip={},{}&units={}&lang={}&cnt={}" \
                        .format(weather_option, location, country, units, language, counter)

                else:  # If it is a city name
                    query = "{}?q={},{}&units={}&lang={}&cnt={}" \
                        .format(weather_option, location, country, units, language, counter)
                weather_data = get_weather_data(query, config)
                display_results(weather_data, str(user_selection))

            elif user_selection == "3":
                # TODO // Make a better config editor and make it it's own function
                # Open and edit the config file
                print()
                make_change = input("Configuration: \n 1: units: ({0}) \n 2: country: ({1})\n 3: language: "
                                    "({2})\n 4: API Key: ({3})\n Please select the config you wish to change: "
                                    .format(units, country, language, api_key))
                if make_change == "1":
                    temp_setting = input("Please select either F, C, or K: ")
                    if temp_setting.lower() == "f":
                        units = "imperial"
                    elif temp_setting.lower() == "c":
                        units = "metric"
                    elif temp_setting.lower() == "k":
                        units = 'kelvin'

                elif make_change == "2":
                    new_country = input("Please select a country using a two character country code: ").upper()[0:2]
                    if new_country not in ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CD', 'CG', 'CK', 'CR', 'HR', 'CU', 'CW', 'CY', 'CZ', 'CI', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'MK', 'RO', 'RU', 'RW', 'RE', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'US', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'AX']:
                        print("Country not found!")
                    else:
                        country = new_country

                elif make_change == "3":
                    # https://openweathermap.org/current#multi
                    language = input("Please select a language using a two character language code: ").upper()[0:2]

                elif make_change == "4":
                    api_key_new = input("Please enter a new API key: ")
                    complete_url = "{}weather?zip={},{}&appid={}".format(config.base_url, "11210", "US", api_key_new)
                    response = requests.get(complete_url)
                    if response.status_code == 200:
                        print("Successfully connected to the API")
                        api_key = api_key_new
                    elif response.status_code == 401:
                        print("Invalid API key. Please try again!")

                else:
                    continue
                if language == config.language \
                        and country == config.country \
                        and units == config.units \
                        and api_key == config.api_key:
                    pass
                else:
                    config_file = open("config.ini", "w")
                    config_file.write("[openweathermap]\n")
                    config_file.write("api_key={}\n".format(api_key))
                    config_file.write("units={}\n".format(units))
                    config_file.write("country={}\n".format(country))
                    config_file.write("language={}\n".format(language))
                    config_file.write("base_url=http://api.openweathermap.org/data/2.5/")
                    config_file.close()
                    "Configuration Saved!"
                    config = get_config()

            elif user_selection == "4":
                print("Goodbye!")
                exit()

            else:
                print("Invalid Request: Please try again")

    except ValueError:
        raise ValueError
    except SyntaxError:
        raise SyntaxError


if __name__ == '__main__':
    main()
