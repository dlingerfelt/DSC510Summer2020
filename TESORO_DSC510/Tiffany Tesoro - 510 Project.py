#DSC 510

#Week 10

#Final Project

#Author Tiffany Tesoro

#08/09/2020

#TO USE API TO GET DATA
import json
import requests
#Use the Requests library in order to request data from the webservice.

#DEFINE USER_INPUT FUNCTION
def user_input():
    print()
    #Create a Python Application which asks the user for their zip code or city.
    #originally had separate functions for user to choose from current weather OR 5-day weather AND
    #city OR zipcode search, but found it easier to combine the two questions into one function
    while True:
        forecast_type = input('Please input one of the following numbers then press enter: \n'
                              '1 - search for CURRENT weather forecast by zip code \n'
                              '2 - search for CURRENT weather forecast by city \n'
                              '3 - search for 5-DAY weather forecast by zip code \n'
                              '4 - search for 5-DAY weather forecast by city \n')
        if forecast_type == '1':
            #CALL TO ZIP_CURRENT FUNCTION
            zip_current()
        elif forecast_type == '2':
            #CALL TO CITY_CURRENT FUNCTION
            city_current()
        elif forecast_type == '3':
            #CALL TO ZIP_FORECAST FUNCTION
            zip_forecast()
        elif forecast_type == '4':
            #CALL TO CITY_FORECAST FUNCTION
            city_forecast()
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue

#DEFINE ANOTHER_INPUT FUNCTION
def another_input():
    #Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
    while True:
        another_selection = input(
            'Would you like to look for another weather forecast? Type Y [OR] N then press enter.\n').lower()
        if another_selection == 'y':
            #CALL TO USER_INPUT FUNCTION
            user_input()
        elif another_selection == 'n':
            #GOODBYE GREETING
            print()
            print(
                '--- Thank you for using the OpenWeather Forecast Application. Have a wonderful day! ---')
            exit()
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue

#DEFINE ZIP_CURRENT FUNCTION
#to avoid repetitiveness, most comments are made in zip_current function
#but they are applicable to city_current/zip_forecast/city_forecast too
def zip_current():
    print()
    #Use the zip code in order to obtain weather forecast data from OpenWeatherMap.
    print()
    zip_input = input('Type in a zip code then press enter: \n')
    #change input to string to append to url
    zip_code = str(zip_input)
    #base url for search type
    zip_current_url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip_code + ',us'
    while True:
        lang_input = input(
            'Please type in a preferred language code for display results then press enter - ex. for English put EN [OR] for Spanish put ES: \n').upper()
        #Validate whether the user entered valid data. If valid data isn’t presented notify the user.
        #language options - if/elif/else statements to ensure question is answered correctly and direct to next step
        #for all list items included in program, i found it easier to put it after 'in' instead of a separate variable like lang = ['AF', etc.]
        if lang_input in ['AF', 'AL', 'AR', 'BG', 'CA', 'CZ', 'DA', 'DE', 'EL', 'EN', 'EU', 'FA', 'FI', 'FR', 'GL',
                          'HE', 'HI', 'HR', 'HU', 'ID', 'IT', 'JA', 'KR', 'LA', 'LT', 'MK', 'NO', 'NL', 'PL', 'PT',
                          'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN',
                          'PT_BR', 'RO', 'RU', 'SV', 'SE', 'SK', 'SL', 'SP', 'ES', 'SR', 'TH', 'TR', 'UA', 'UK', 'VI',
                          'ZH_CN', 'ZH_TW', 'ZU']:
            #updates url with added elements
            zip_current_url = zip_current_url + '&lang=' + lang_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        #unit options
        unit_input = input(
            'Please enter a preferred unit, imperial [OR] metric, for display results then press enter: \n').lower()
        if unit_input == 'imperial':
            zip_current_url = zip_current_url + '&units=' + unit_input
            break
        elif unit_input == 'metric':
            zip_current_url = zip_current_url + '&units=' + unit_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    api_key = '&appid=3da266a93ce5e67bd3cd607043e5863f'
    zip_url = zip_current_url + api_key
    zip_response = requests.get(zip_url)
    #Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
    data = zip_response.text
    parsed = json.loads(data)
    try:
        #REFERENCE - https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/
        #i tried to use a nested dictionary FOR LOOP to print data but had trouble finding the key-value pairs
        #for i in parsed['weather']:
            #print("Description:", i['description'])
        #description printed correct information, but the others i did not end up figuring out so used a different printing method
        #REFERENCE - https://stackoverflow.com/questions/52808939/python-parsing-and-iterating-through-json-data
        #in order to get the right keys, i had to run program multiple times til i got the right combination
        #might not be the most efficient way, but it was what worked for me
        city = parsed['name']
        zip_desc = parsed['weather'][0]['description']
        zip_temp = parsed['main']['temp']
        zip_feel = parsed['main']['feels_like']
        zip_min = parsed['main']['temp_min']
        zip_max = parsed['main']['temp_max']
        zip_humid = parsed['main']['humidity']
        zip_cloud = parsed['clouds']['all']
        zip_wind = parsed['wind']['speed']
        print()
        #Display the weather forecast in a readable format to the user.
        print('--- Current Weather for ' + city + ' ---')
        print('Description: ' + zip_desc)
        print('Current Temperature: ' + str(zip_temp))
        print('Feels Like: ' + str(zip_feel))
        print('Temperature Low: ' + str(zip_min))
        print('Temperature High: ' + str(zip_max))
        print('Humidity: ' + str(zip_humid))
        print('Cloud Cover: ' + str(zip_cloud))
        print('Wind speed: ' + str(zip_wind))
        print()
        print()
        # CALL TO ANOTHER_INPUT FUNCTION
        another_input()
    except ValueError:
        print("Zip code not found. Please try again.")
        print()
        print()

#DEFINE CITY_CURRENT FUNCTION
def city_current():
    print()
    #Use the city name in order to obtain weather forecast data from OpenWeatherMap.
    print()
    city_input = input('Type in a city name then press enter - ex. New York: \n').upper()
    city_current_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_input
    while True:
        state_input = input(
            'Type in a state code then press enter - ex. FL (if the city is outside of the United States, please type in US for default setting): \n').upper()
        if state_input in ['AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                               'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO',
                               'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR',
                               'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'US'] :
            city_current_url = city_current_url + ',' + state_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        country_input = input('Type in a country code then press enter - ex. FR: \n').upper()
        if country_input in ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ',
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
                               'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'AX'] :
            city_current_url = city_current_url + ',' + country_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        lang_input = input(
            'Please enter a preferred language code for display results then press enter - ex. for English type EN [OR] for Spanish type in ES: \n').upper()
        if lang_input in ['AF', 'AL', 'AR', 'BG', 'CA', 'CZ', 'DA', 'DE', 'EL', 'EN', 'EU', 'FA', 'FI', 'FR', 'GL',
                               'HE', 'HI', 'HR', 'HU', 'ID', 'IT', 'JA', 'KR', 'LA', 'LT', 'MK', 'NO', 'NL', 'PL', 'PT',
                               'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN',
                               'PT_BR', 'RO', 'RU', 'SV', 'SE', 'SK', 'SL', 'SP', 'ES', 'SR', 'TH', 'TR', 'UA', 'UK', 'VI',
                               'ZH_CN', 'ZH_TW', 'ZU']:
            city_current_url = city_current_url + '&lang=' + lang_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        unit_input = input(
            'Please enter a preferred unit, imperial [OR] metric, for display results then press enter: \n').lower()
        if unit_input == 'imperial':
            city_current_url = city_current_url + '&units=' + unit_input
            break
        elif unit_input == 'metric':
            city_current_url = city_current_url + '&units=' + unit_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    api_key = '&appid=3da266a93ce5e67bd3cd607043e5863f'
    city_url = city_current_url + api_key
    city_response = requests.get(city_url)
    data = city_response.text
    parsed = json.loads(data)
    try:
        city_desc = parsed['weather'][0]['description']
        city_temp = parsed['main']['temp']
        city_feel = parsed['main']['feels_like']
        city_min = parsed['main']['temp_min']
        city_max = parsed['main']['temp_max']
        city_humid = parsed['main']['humidity']
        city_cloud = parsed['clouds']['all']
        city_wind = parsed['wind']['speed']
        print()
        #Display the weather forecast in a readable format to the user.
        print('--- Current Weather for ' + city_input + ', ' + state_input + ', ' + country_input + ' ---')
        print('Description: ' + city_desc)
        print('Current Temperature: ' + str(city_temp))
        print('Feels Like: ' + str(city_feel))
        print('Temperature Low: ' + str(city_min))
        print('Temperature High: ' + str(city_max))
        print('Humidity: ' + str(city_humid))
        print('Cloud Cover: ' + str(city_cloud))
        print('Wind speed: ' + str(city_wind))
        print()
        print()
        # CALL TO ANOTHER_INPUT FUNCTION
        another_input()
    except ValueError:
        print("Zip code not found. Please try again.")
        print()
        print()

#DEFINE ZIP_FORECAST FUNCTION
def zip_forecast():
    print()
    #Use the zip code in order to obtain weather forecast data from OpenWeatherMap.
    print()
    zip_input = input('Type in a zip code then press enter: \n')
    zip_code = str(zip_input)
    zip_current_url = 'http://api.openweathermap.org/data/2.5/forecast?zip=' + zip_code + ',us'
    while True:
        lang_input = input(
            'Please enter a preferred language code for display results then press enter - ex. for English type EN [OR] for Spanish type in ES: \n').upper()
        if lang_input in ['AF', 'AL', 'AR', 'BG', 'CA', 'CZ', 'DA', 'DE', 'EL', 'EN', 'EU', 'FA', 'FI', 'FR', 'GL',
                          'HE', 'HI', 'HR', 'HU', 'ID', 'IT', 'JA', 'KR', 'LA', 'LT', 'MK', 'NO', 'NL', 'PL', 'PT',
                          'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN',
                          'PT_BR', 'RO', 'RU', 'SV', 'SE', 'SK', 'SL', 'SP', 'ES', 'SR', 'TH', 'TR', 'UA', 'UK', 'VI',
                          'ZH_CN', 'ZH_TW', 'ZU']:
            zip_current_url = zip_current_url + '&lang=' + lang_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        unit_input = input(
            'Please enter a preferred unit, imperial [OR] metric, for display results then press enter: \n').lower()
        if unit_input == 'imperial':
            zip_current_url = zip_current_url + '&units=' + unit_input
            break
        elif unit_input == 'metric':
            zip_current_url = zip_current_url + '&units=' + unit_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    api_key = '&appid=3da266a93ce5e67bd3cd607043e5863f'
    zip_url = zip_current_url + api_key
    zip_response = requests.get(zip_url)
    data = zip_response.text
    parsed = json.loads(data)
    try:
        #similar to previous comment, this might not be the most efficient but it was what worked for me at the moment
        #min/max were chosen based on approximate highest/lowest temperature when viewing API in web browser
        #i'm not sure whether they are the true high/low because the data is always being updated
        date_one = parsed['list'][5]['dt_txt']
        desc_one = parsed['list'][5]['weather'][0]['description']
        max_one = parsed['list'][5]['main']['temp_max']
        min_one = parsed['list'][2]['main']['temp_min']
        date_two = parsed['list'][13]['dt_txt']
        desc_two = parsed['list'][13]['weather'][0]['description']
        max_two = parsed['list'][13]['main']['temp_max']
        min_two = parsed['list'][10]['main']['temp_min']
        date_three = parsed['list'][21]['dt_txt']
        desc_three = parsed['list'][21]['weather'][0]['description']
        max_three = parsed['list'][21]['main']['temp_max']
        min_three = parsed['list'][18]['main']['temp_min']
        date_four = parsed['list'][29]['dt_txt']
        desc_four = parsed['list'][29]['weather'][0]['description']
        max_four = parsed['list'][29]['main']['temp_max']
        min_four = parsed['list'][26]['main']['temp_min']
        date_five = parsed['list'][37]['dt_txt']
        desc_five = parsed['list'][37]['weather'][0]['description']
        max_five = parsed['list'][37]['main']['temp_max']
        min_five = parsed['list'][34]['main']['temp_min']
        print()
        print()
        #Display the weather forecast in a readable format to the user.
        #originally printed temperature min/max as separate from each other but sometimes data would print with values switched
        #i'm not sure why even though in the web browser i checked multiple times that temp_max and temp_min were correct
        #range at least ensures a rough estimate temperature but i know it is technically not accurate
        print('--- 5-DAY FORECAST FOR ' + zip_code + ' ---')
        print()
        print('TOMORROW')
        print(str(date_one))
        print('Description: ' + desc_one)
        print('Approximate Temperature Range: ' + str(max_one) + ' to ' + str(min_one))
        print()
        print('2 DAYS FROM TODAY')
        print(str(date_two))
        print('Description: ' + desc_two)
        print('Approximate Temperature Range: ' + str(max_two) + ' to ' + str(min_two))
        print()
        print('3 DAYS FROM TODAY')
        print(str(date_three))
        print('Description: ' + desc_three)
        print('Approximate Temperature Range: ' + str(max_three) + ' to ' + str(min_three))
        print()
        print('4 DAYS FROM TODAY')
        print(str(date_four))
        print('Description: ' + desc_four)
        print('Approximate Temperature Range: ' + str(max_four) + ' to ' + str(min_four))
        print()
        print('5 DAYS FROM TODAY')
        print(str(date_five))
        print('Description: ' + desc_five)
        print('Approximate Temperature Range: ' + str(max_five) + ' to ' + str(min_five))
        print()
        print()
        # CALL TO ANOTHER_INPUT FUNCTION
        another_input()
    except ValueError:
        print("Zip code not found. Please try again.")
        print()
        print()

#DEFINE CITY_FORECAST FUNCTION
def city_forecast():
    print()
    #Use the city name in order to obtain weather forecast data from OpenWeatherMap.
    print()
    city_input = input('Type in a city name then press enter - ex. New York: \n').upper()
    city_current_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_input
    while True:
        state_input = input(
            'Type in a state code then press enter - ex. FL (if the city is outside of the United States, please type in US for default setting): \n').upper()
        if state_input in ['AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                           'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO',
                           'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR',
                           'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'US']:
            city_current_url = city_current_url + ',' + state_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        country_input = input('Type in a country code then press enter - ex. FR: \n').upper()
        if country_input in ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ',
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
            city_current_url = city_current_url + ',' + country_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        lang_input = input(
            'Please enter a preferred language code for display results then press enter - ex. for English type EN [OR] for Spanish type in ES: \n').upper()
        if lang_input in ['AF', 'AL', 'AR', 'BG', 'CA', 'CZ', 'DA', 'DE', 'EL', 'EN', 'EU', 'FA', 'FI', 'FR', 'GL',
                          'HE', 'HI', 'HR', 'HU', 'ID', 'IT', 'JA', 'KR', 'LA', 'LT', 'MK', 'NO', 'NL', 'PL', 'PT',
                          'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN',
                          'PT_BR', 'RO', 'RU', 'SV', 'SE', 'SK', 'SL', 'SP', 'ES', 'SR', 'TH', 'TR', 'UA', 'UK', 'VI',
                          'ZH_CN', 'ZH_TW', 'ZU']:
            city_current_url = city_current_url + '&lang=' + lang_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    while True:
        unit_input = input(
            'Please enter a preferred unit, imperial [OR] metric, for display results then press enter: \n').lower()
        if unit_input == 'imperial':
            city_current_url = city_current_url + '&units=' + unit_input
            break
        elif unit_input == 'metric':
            city_current_url = city_current_url + '&units=' + unit_input
            break
        else:
            print('Invalid response. Please try again.')
            print()
            print()
            continue
    api_key = '&appid=3da266a93ce5e67bd3cd607043e5863f'
    city_url = city_current_url + api_key
    city_response = requests.get(city_url)
    data = city_response.text
    parsed = json.loads(data)
    try:
        date_one = parsed['list'][5]['dt_txt']
        desc_one = parsed['list'][5]['weather'][0]['description']
        max_one = parsed['list'][2]['main']['temp_max']
        min_one = parsed['list'][5]['main']['temp_min']
        date_two = parsed['list'][13]['dt_txt']
        desc_two = parsed['list'][13]['weather'][0]['description']
        max_two = parsed['list'][10]['main']['temp_max']
        min_two = parsed['list'][13]['main']['temp_min']
        date_three = parsed['list'][21]['dt_txt']
        desc_three = parsed['list'][21]['weather'][0]['description']
        max_three = parsed['list'][18]['main']['temp_max']
        min_three = parsed['list'][21]['main']['temp_min']
        date_four = parsed['list'][29]['dt_txt']
        desc_four = parsed['list'][29]['weather'][0]['description']
        max_four = parsed['list'][26]['main']['temp_max']
        min_four = parsed['list'][29]['main']['temp_min']
        date_five = parsed['list'][37]['dt_txt']
        desc_five = parsed['list'][37]['weather'][0]['description']
        max_five = parsed['list'][34]['main']['temp_max']
        min_five = parsed['list'][37]['main']['temp_min']
        print()
        print()
        #Display the weather forecast in a readable format to the user.
        print('--- 5-DAY FORECAST FOR ' + city_input + ', ' + state_input + ', ' + country_input + ' ---')
        print()
        print('TOMORROW')
        print(date_one)
        print('Description: ' + desc_one)
        print('Approximate Temperature Range: ' + str(max_one) + ' to ' + str(min_one))
        print()
        print('2 DAYS FROM TODAY')
        print(date_two)
        print('Description: ' + desc_two)
        print('Approximate Temperature Range: ' + str(max_two) + ' to ' + str(min_two))
        print()
        print('3 DAYS FROM TODAY')
        print(date_three)
        print('Description: ' + desc_three)
        print('Approximate Temperature Range: ' + str(max_three) + ' to ' + str(min_three))
        print()
        print('4 DAYS FROM TODAY')
        print(date_four)
        print('Description: ' + desc_four)
        print('Approximate Temperature Range: ' + str(max_four) + ' to ' + str(min_four))
        print()
        print('5 DAYS FROM TODAY')
        print(date_five)
        print('Description: ' + desc_five)
        print('Approximate Temperature Range: ' + str(max_five) + ' to ' + str(min_five))
        print()
        print()
        #CALL TO ANOTHER_INPUT FUNCTION
        another_input()
    except ValueError:
        print("Zip code not found. Please try again.")
        print()
        print()

#DEFINE MAIN FUNCTION
def main():
    #HELLO GREETING
    print()
    print('--- Welcome to the OpenWeather Forecast Application! ---')
    #Use functions including a main function.
    #CALL TO USER_INPUT FUNCTION
    user_input()

#CALL TO MAIN FUNCTION
if __name__ == "__main__":
    main()