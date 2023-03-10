# Weather Finder

The Weather Finder is a Python script that retrieves the current weather of each city listed in a provided CSV file using the OpenWeatherMap API. It prints a running list of JSONs for each city in the console and saves the city names and temperatures in a new CSV file.

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
3. Create a new CSV file called `cities.txt` in the repository directory.
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

## Contributing
If you would like to contribute to the Weather Finder project, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.
