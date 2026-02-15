import requests
import dotenv
import os
# I will implement rain alert using sms and openweather api

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
dotenv.load_dotenv()

api_key = os.getenv(key="API_KEY")
lon = os.getenv(key="LON")
lat = os.getenv(key="LAT")


# parameter = {
#     "lat": lat,
#     "lon": lon,
#     "appid": api_key
# }

response = requests.get(url=f"{ENDPOINT}?lat={lat}&lon={lon}&appid={api_key}")

response.raise_for_status()

data = None
if response.status_code == 200:
    data = response.json()

print(data)