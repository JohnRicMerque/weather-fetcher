# Weather Fetcher using Python and weather API
# YT tutorial Video: https://www.youtube.com/watch?v=Oz3W-LKfafE&ab_channel=TechWithTim

# Pseudocode
# get weather data from API
# install request module
# initialize API key and Base URL

import requests

API_KEY = "4d7436b2e953a39a0d36c842e7742e02"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# asks user input of city to integrate into the URL with API 
city_name = input("What city do you want to look into?: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}"

# request module method to get request url
response = requests.get(request_url)

# check if response is successful
if response.status_code == 200: # if successful transform API into JSON format 
    data = response.json()

    # accessing keys and printing them
    weather = data['weather']
    print(weather)

    temperature = data['main']['temp']
    print(temperature)

else:
    print("An error occured! Please try again later")


