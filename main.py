import requests
import dotenv
import os
import pprint
# I will implement rain alert using sms and openweather api

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
dotenv.load_dotenv()

api_key = os.getenv(key="API_KEY")
lon = os.getenv(key="LON")
lat = os.getenv(key="LAT")


parameter = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=ENDPOINT, params=parameter)

response.raise_for_status()

data = response.json()

# get data 
pprint.pprint(data)
for weather in data["list"]:
    code = weather["weather"][0]["id"]

    if code <700:
        print(f"Bring up your umbrella {code}")