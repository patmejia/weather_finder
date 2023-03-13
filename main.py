# main.py

import requests as req

def test_api_key():
    with open('setup/api_key.txt', 'r') as f:
        api_key = f.read().strip()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=' + api_key
    r = req.get(url)
    if r.status_code == 200:
        return True
    else:
        return False

# test_main.py

import main
import pytest

def test_api_key():
    assert main.test_api_key() is True, "API key test failed"
