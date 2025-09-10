'''
Name: Daniel Nguyen
Date: September 8, 2025
Description: A simple weather application that fetches and displays current weather information for a given city using the OpenWeatherMap API.
'''

import requests

API_KEY = 'd83535c0145153cb67a28d392bb95e73' # OpenWeatherMap API key

def get_weather(city):

    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial'

    response = requests.get(base_url)

    temperature = response.json()['main']['temp']
    temp_high = response.json()['main']['temp_max']
    temp_low = response.json()['main']['temp_min']
    location = response.json()['name']
    condition = response.json()['weather'][0]['description']

    return f"In {location}, it is currently {temperature}°F with {condition} and a high of {temp_high}°F and a low of {temp_low}°F."

def get_city():
    city = input("Enter city name for weather information: ")

    return get_weather(city)

def main():
    print(get_city())

if __name__ == "__main__":

    main()