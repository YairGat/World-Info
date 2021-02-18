# Yair Gat 18.2.2021
# This file represents the server side.
import socket
import json
from datetime import datetime
import pytz
import pyowm
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from City import City

"""
Return the api of 'Open Weather Map' website.
https://openweathermap.org/
"""


def get_API():
    return '68104af36e614bf023b559db776769b6'


def get_obs(city):
    owm = pyowm.OWM(get_API())
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(city)
    return obs


"""
Gets city and return the time zone of that city
"""


def find_time_zone(city):
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # input as a geek
    lad = city
    print("Location address:", lad)

    # getting Latitude and Longitud
    location = geolocator.geocode(lad)

    print("Latitude and Longitude of the said address:")
    print((location.latitude, location.longitude))
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    return result


""""
Gets city and return the current time in this city.
"""


def get_time(city):
    timeZ = pytz.timezone(find_time_zone(city))
    dt = str(datetime.now(timeZ).time())
    dt = dt.split('.')[0]
    return 'The time in %s is: %s ' % (city, dt)


""""
Get city and return the weather in this city.
"""


def get_weather(city):
    return 'The weather in %s is: %s ' % (city, get_obs(city).weather.temperature(unit='celsius'))


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
cities = City()
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        flag = 0  # The flag is 0 as long as the client has not exit the program and 1 when the client exits.
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode() == 'close':
                    flag = 1
                    break
                data = json.loads(data.decode())
                if data.get("InfoType") == 'Time':
                    conn.sendall(bytes(get_time(data.get("City")), 'utf-8'))
                elif data.get("InfoType") == 'Weather':
                    conn.sendall(bytes(get_weather(data.get("City")), 'utf-8'))
                elif data.get("InfoType") == "Local News":
                    conn.sendall(bytes(cities.get_local_news(data.get("City")), 'utf-8'))
                else:
                    conn.sendall(bytes("Please Chose information type you want to know."), 'utf-8')

        if flag == 1:  # True if the client exited from the program.
            break
