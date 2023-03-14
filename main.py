import requests as req
import json
import csv
from typing import List, Dict, Any

def get_api_key(api_key_path: str) -> str:
    with open(api_key_path, "r") as f:
        api_key = f.read().strip()
    return api_key

def read_csv_file(csv_file_path: str) -> List[str]:
    cities = []
    with open(csv_file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cities.append(row[0])
    return cities

def get_city_weather(city: str, api_key: str) -> Dict[str, Any]:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = req.get(url)
    weather_data = json.loads(response.text)
    return weather_data

def write_to_csv(city_temperatures: Dict[str, float], csv_file_path: str) -> None:
    with open(csv_file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["City", "Temperature"])
        for city, temperature in city_temperatures.items():
            writer.writerow([city, temperature])

def test_api_key() -> bool:
    api_key_path = "setup/api_key.txt"
    api_key = get_api_key(api_key_path)
    return isinstance(api_key, str) and len(api_key) == 32

if __name__ == "__main__":
    # Specify API key path and CSV file path
    api_key_path = "setup/api_key.txt"
    csv_file_path = "input/cities.csv"

    # Retrieve API key
    api_key = get_api_key(api_key_path)

    # Read CSV file
    cities = read_csv_file(csv_file_path)

    # Retrieve weather data for each city and write to CSV file
    city_temperatures = {}
    for city in cities:
        weather_data = get_city_weather(city, api_key)
        temperature = weather_data["main"]["temp"]
        city_temperatures[city] = temperature


# Print city name and temperature to console with color and emoji
    for city, temperature in city_temperatures.items():
        if temperature < 50:
            color = "\033[94m"  # blue
            emoji = "🧊"
        elif temperature < 70:
            color = "\033[92m"  # green
            emoji = "🌱"
        else:
            color = "\033[91m"  # red
            emoji = "♨️"
        print(f"{city:<20} {color}{temperature:>5.1f}°F {emoji}\033[0m")


    # Write to CSV file    
    write_to_csv(city_temperatures, "output/output.csv")
