# python_weather_finder

import requests
import json
import sys

# Get the API key from the file
with open('api_key.txt', 'r') as f:
    api_key = f.read()
    


# Get the city name from the command line
city = sys.argv[1]

# Get the weather data from the API
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)
r = requests.get(url)
data = r.json()

# Get the temperature in Celsius
temp = data['main']['temp'] - 273.15

# Get the weather description
weather = data['weather'][0]['description']

# Get the wind speed
wind_speed = data['wind']['speed']

# Print the output
print('Temperature: {:.2f}°C'.format(temp))
print('Weather: {}'.format(weather))
print('Wind Speed: {} m/s'.format(wind_speed))

# Path: weather finder_python/api_key.txt
# 1234567890

# Path: weather finder_python/requirements.txt
# requests

# Path: weather finder_python/README.md
# # Weather Finder

# A simple Python script to get the weather of a city.

# ## Usage

# ```bash
# python main.py <city>
# ```

# ## Example

# ```bash
# python main.py London
# ```
# Temperature: 10.00°C
# Weather: clear sky
# Wind Speed: 3.6 m/s

# ## Requirements

# - Python 3
# - requests

# ## License

# MIT

# ## Author

# [Sourav Singh](https://souravsingh.com)

# ## Acknowledgements

# - [OpenWeatherMap](https://openweathermap.org/)

# ## Disclaimer

# This project is for educational purposes only.

# ## Contributing

# Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Please make sure to update tests as appropriate.

# ## Support

# If you like this project, please consider supporting me on [Patreon](https://www.patreon.com/souravsingh).

# ## Donate

# If you would like to donate, you can do so via [PayPal](https://www.paypal.me/souravsingh).

# ## Contact

# If you have any questions, feel free to contact me at [

# Path: weather finder_python/.gitignore
# __pycache__/
# *.pyc
# *.pyo
# *.pyd
# *.so
# *.egg
# *.egg-info
# *.exe
# *.dll
# *.obj
# *.manifest
# *.log
# *.pot