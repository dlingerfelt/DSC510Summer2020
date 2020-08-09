# Katie Simek
# 09/08/2020
# Create a program that uses the Request library to make a GET request of
# the specified API.  Parse and format the response to print the
# "value" key to the user.  Allow the program to be repeated until the user
# terminates the program.

import requests


# Function to get the latitude and longitude of the given city or zipcode
def location(city):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="final_project")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


# Function to print the future forecast based on number of days requested
def future_forecast(days, forecast):
    d = 0
    while d <= days:
        if d < 1:
            print('-->Today\'s forecast: ')
        if d == 1:
            print('-->Tomorrow\'s forecast: ')
        if d >= 2:
            print('-->Day', d, ' forecast: ')
        print('    Daily high is', forecast['daily'][d]['temp']['max'], ''
              'degrees Farenheit.')
        print('    Daily low is', forecast['daily'][d]['temp']['min'], ''
              'degrees Farenheit.')
        print('    With ', forecast['daily'][d]['weather'][0]['description'])
        print()
        d += 1


def main():
    # Welcome greeting
    print('Hello and welcome to the weather forecaster.')
    # Ask user for the city to be forecasted
    while True:
        city = input('Please enter the city or zip code to get the current '
                     'weather forecast:\n')
        location.latitude, location.longitude = location(city)
        lat = location.latitude
        lon = location.longitude
        part = 'minutely',
        appid = '25d8873927f1921d95e7eb71ec0d9343'
        while True:
            response = requests.get('https://api.openweathermap.org/data/2.5/'
                                    'onecall?lat={}&lon={}&units=imperial&exclude'
                                    '={}&appid={}'.format(lat, lon, part, appid))
            try:
                forecast = response.json()
                break
            except requests.exceptions.HTTPError:
                print('There was an HTTP Error with your request). Please try again.')
                continue
            except requests.exceptions.ConnectionError:
                print('There was a Connection Error with your request. Please try again.')
                continue
            except requests.exceptions.Timeout:
                print('There was a Timeout Error with your request. Please try again.')
                continue
            except requests.exceptions.RequestException:
                print('There was an error with your request. Please try again.')
                continue
        print()
        print('The current temperature is: ', forecast['current']['temp'], ''
              'degrees Farenheit.')
        print()
        future = input('Would you like a future forecast for this same location?\n'
                       'Please enter "Yes" or "No". ')
        future = future.lower()
        if future == str('yes'):
            while True:
                print()
                days = input('Please enter the number of days you would like forecast.\n'
                             'Enter "0" to see today\'s forecast.\n'
                             'Enter values "1" - "7" for the next seven days. ')
                print()
                try:
                    days = int(days)
                    if 0 < days <= 7:
                        break
                    if days >= 8:
                        print('Invalid entry. Please select a number of days'
                              ' less than eight.')
                        continue
                except ValueError:
                    print('*Error*. Please enter a valid number of days.')
                    break
            # Utilize the function to print the forecast for the future days
            future_forecast(days, forecast)
        if future == str('no'):
            pass
        print()
        city_2 = input('Would you like a forecast for a different location?\n'
                       'Please enter "Yes" or "No". ')
        print()
        city_2 = city_2.lower()
        if city_2 == str('yes'):
            continue
        if city_2 == str('no'):
            print('Okay.  Goodbye.')
            quit()
        # Return error for invalid entry to initial question
        else:
            print('**** Invalid entry. ****\n'
                  'Please enter "Yes" or "No".\n')
            continue


if __name__ == "__main__":
    main()
