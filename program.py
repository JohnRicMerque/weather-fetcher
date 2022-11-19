# John Ric Merque | BSCOE 2-6 | Weather Fetcher using Python and weather API
# This program is referenced to YT tutorial Video: https://www.youtube.com/watch?v=Oz3W-LKfafE&ab_channel=TechWithTim. I made some slight modifications to improve the program.

# Pseudocode
# get weather data from API
# install request module
# initialize API key and Base URL

import requests

API_KEY = "4d7436b2e953a39a0d36c842e7742e02"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True: 
    # asks user input of city to integrate into the URL with API 
    city_name = input("What city do you want to look into?: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}"

    # request module method to get request url
    response = requests.get(request_url)

    # check if response is successful
    if response.status_code == 200: # if successful transform API into JSON format 
        data = response.json()

        # accessing keys
        weather = data['weather'][0]["description"]
        temperature = round(data['main']['temp'] - 273.15)
        feels_like = round(data['main']['feels_like'] - 273.15)
        wind_speed = data['wind']['speed']

        # display 
        print(f"{city_name.title()} is having {weather}.")
        print(f"The current temperature in the city is {temperature}°C.")
        print(f"But it would feel like {feels_like}°C.")
        print(f"While the current wind speed in the area is {wind_speed}m/s.")
        print(f"That's all, Stay Safe!")

    else:
        print("An error occured! Please try again")
    
    exitProgram = input('Do you wish to check the weather on another city? (y/n): ')
    if exitProgram.lower() == 'y':
        continue
    elif exitProgram.lower() == 'n':
        print("Thank you for trusting us! Bye")
        break
    else:
        print("Thank you for trusting us, Bye!")
        break



