import requests
import dotenv
import os
import pprint
import os
from twilio.rest import Client
# I will implement rain alert using sms and openweather api

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
dotenv.load_dotenv()

api_key = os.getenv(key="API_KEY")
lon = float(os.getenv(key="LON"))
lat = float(os.getenv(key="LAT"))

account_sid  = os.getenv(key="ACCOUNT_SID")
auth_token  = os.getenv(key="AUTH_TOKEN")

# print(type(lon))
parameter = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 8
}

response = requests.get(url=ENDPOINT, params=parameter)

response.raise_for_status()

data = response.json()

# get data 
# pprint.pprint(data)
is_raining = False

for weather in data["list"]:
    code = int(weather["weather"][0]["id"])
    code =  600
    # print(code)

    if code <700:
        is_raining = True
        break

message = None
if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Bring your umbrella, Cause it's about to rain",
    from_="+12566854735",
    to="+27607047759",
    )

print(message.status)