import socket
import json
from datetime import datetime
import pytz
import pyowm
from geopy import geocoders
from timezonefinder import TimezoneFinder
import tzwhere
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from City import Capitals


def get_API():
    return '68104af36e614bf023b559db776769b6'


def get_obs(city):
    owm = pyowm.OWM(get_API())
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(city)
    return obs


def find_time_zone(city):
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # input as a geek
    lad = "Washington"
    print("Location address:", lad)

    # getting Latitude and Longitud
    location = geolocator.geocode(lad)

    print("Latitude and Longitude of the said address:")
    print((location.latitude, location.longitude))

    # pass the Latitude and Longitud
    # into a timezone_at
    # and it return timezone
    obj = TimezoneFinder()

    # returns 'Europe/Berlin'
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    return result


def get_time(city):
    timeZ = pytz.timezone(find_time_zone(city))
    dt = str(datetime.now(timeZ).time())
    dt = dt.split('.')[0]
    return 'The time in %s is: %s ' % (city, dt)


def get_weather(city):
    return 'The weather in %s is: %s ' % (city, get_obs(city).weather.temperature(unit='celsius'))


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
capitals = Capitals()
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        flag = 0
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
                    conn.sendall(bytes(get_time(data.get("Capital")), 'utf-8'))
                elif data.get("InfoType") == 'Weather':
                    conn.sendall(bytes(get_weather(data.get("Capital")), 'utf-8'))
                else:
                    conn.sendall(bytes("local news"), 'utf-8')
        if flag == 1:
            break