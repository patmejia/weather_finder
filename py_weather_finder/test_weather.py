# Install dependencies: `pip install -r requirements.txt`
# Run: `python test.py`

import weather
import csv

def test_get_weather_data():
    # Specify File Path
    csvpath = "cities.csv"

    # Read CSV
    with open(csvpath) as csvfile:
        # Read the file specifying commas as delimiters
        csvreader = csv.reader(csvfile, delimiter=",")

        # Iterate through each row of the CSV
        for row in csvreader:
            city = row[0]
            weather_data = weather.get_weather_data(city)
            assert isinstance(weather_data, dict)
            assert "main" in weather_data
            assert "temp" in weather_data["main"]
