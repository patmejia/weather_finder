# Weather Finder

The Weather Finder is a Python script that retrieves the current weather of each city listed in a provided CSV file using the OpenWeatherMap API. It prints a running list of JSONs for each city in the console and saves the city names and temperatures in a new CSV file.

![DALL·E 2023-03-09 20 38 27 -  digital illustration that represents the Weather Finder program  The artwork should feature elements such as cityscapes or landscapes of different ci](https://user-images.githubusercontent.com/92187562/224209208-702669c9-9283-45e8-95bc-f266496803c5.png)

## Dependencies

The Weather Finder requires the following dependencies:

- Python 3.x
- requests
- csv

You can install the requests module using pip by running the following command:

```
pip install requests
```

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal in the repository directory.
3. Create a new CSV file called `cities.csv` in the repository directory.
4. Add the names of the cities you want to retrieve weather data for, each on a separate line.
5. Run the Weather Finder script by running the following command in your terminal:

```
python weather.py
```

The script will print the following JSONs to the console:

```
{...} # JSON for New York
{...} # JSON for London
{...} # JSON for Paris
```

The script will also create a new CSV file called `output.csv` in the repository directory, with the following contents:

```
New York, temperature
London, temperature
Paris, temperature
```

# Other information

## API Key

> The following step is optional and might take 1-2 minutes

The Weather Finder uses the OpenWeatherMap API to retrieve weather data. You will need to create an account and generate an API key to use the API. If the inclued API key is no longer valid, you can generate ypur own API key by creating an account [here](https://home.openweathermap.org/users/sign_up).

Once you create an account and log in, you can quickly generate a new API Key [here](https://home.openweathermap.org/api_keys).

After you generate your API key, you can add it to the Weather Finder by replacing the `API_KEY` variable in `setup/api_key.txt` with your API key.

##

## Contributing

If you would like to contribute to the Weather Finder project, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License

The Weather Finder is licensed under the MIT License. See the LICENSE file for more information.

## Contact

If you have any questions, please contact me at [contact@patimejia.com
](mailto:contact@patimejia.com)

## Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
