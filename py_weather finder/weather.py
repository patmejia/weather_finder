# Dependencies
import requests as req
import json
import csv

# OpenWeather API Key
api_key = "417bfe8effcb6b9aa355a4de24d62458"

# Specify File Path
csvpath = "/cities.csv"

# Build an endpoint URL to the OpenWeatherMap Service
url = "http://api.openweathermap.org/data/2.5/weather?"

# Open output file
output_file = "output.csv"
with open(output_file, "w") as csvfile:
    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Read CSV
    with open(csvpath) as csvfile:

        # Read the file specifying commas as delimiters
        csvreader = csv.reader(csvfile)

        # Iterate through each row of the CSV
        for row in csvreader:

            # Retrieve the city name from the CSV file
            city = row[0]

            # Print each row of the csv
            print(city)

            # Build the query URL for the OpenWeatherMap Service
            query_url = url + "q=" + city + "&appid=" + api_key + "&units=Imperial"

            # Make a request to the OpenWeatherMap Service
            weather_response = req.get(query_url)
            weather_json = weather_response.json()

            # Print the JSON for each
            print(weather_json)

            # Extract the temperature for each city
            temperature = weather_json["main"]["temp"]

            # Print the Temperatures
            print(temperature)

            # Draw a separating line
            print("---------------")

            # Write the contents for each to the output CSV
            csvwriter.writerow([city, temperature])

# make the output file readable
with open(output_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

# Output
# City
# {'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}], 'base': 'stations', 'main': {'temp': 51.8, 'pressure': 1012, 'humidity': 81, 'temp_min': 50, 'temp_max': 53.6}, 'visibility': 10000, 'wind': {'speed': 4.7, 'deg': 80}, 'clouds': {'all': 90}, 'dt': 1541030400, 'sys': {'type': 1, 'id': 5091, 'message': 0.0039, 'country': 'GB', 'sunrise': 1541050284, 'sunset': 1541084762}, 'id': 2643743, 'name': 'London', 'cod': 200}
# 51.8
# ---------------
# City
# {'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}], 'base': 'stations', 'main': {'temp': 51.8, 'pressure': 1012, 'humidity': 81, 'temp_min': 50, 'temp_max': 53.6}, 'visibility': 10000, 'wind': {'speed': 4.7, 'deg': 80}, 'clouds': {'all': 90}, 'dt': 1541030400, 'sys': {'type': 1, 'id': 5091, 'message': 0.0039, 'country': 'GB', 'sunrise': 1541050284, 'sunset': 1541084762}, 'id': 2643743, 'name': 'London', 'cod': 200}s