import requests as req

def get_weather_data(city):
    # OpenWeather API Key from api_key.txt

    # Read API Key from file api_key.txt
    with open("api_key.txt") as f:

        # Remove newline character from API Key
        api_key = f.read().strip()


    # Build an endpoint URL to the OpenWeatherMap Service
    url = "http://api.openweathermap.org/data/2.5/weather?"
    query_url = url + "q=" + city + "&appid=" + api_key+ "&units=Imperial"

    # Make a request to the endpoint url
    weather_response = req.get(query_url)
    weather_json = weather_response.json()

    return weather_json


import csv
from weather import get_weather_data

# Specify File Path
csvpath = "cities.csv"
output_file = "output.csv"

# Open output file for writing
with open(output_file, "w") as csvfile:
    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Read CSV
    with open(csvpath) as csvfile:
        # Read the file specifying commas as delimiters
        csvreader = csv.reader(csvfile, delimiter=",")

        # Iterate through each row of the CSV
        for row in csvreader:
            city = row[0]
            weather_data = get_weather_data(city)
            temperature = weather_data["main"]["temp"]

            # Write city name and temperature to output file
            csvwriter.writerow([city, temperature])

            # Print weather data to console
            print(weather_data)
