from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import pyowm
from timezonefinder import TimezoneFinder

from zoneinfo import ZoneInfo
# APIKEY='68104af36e614bf023b559db776769b6'                  #your API Key here as string
# owm = pyowm.OWM(APIKEY)
# bla = owm.tile_manager()
# mgr = owm.weather_manager()
# obs =mgr.weather_at_place('Washington')
# print(obs.location)
# print(obs.reception_time(timeformat='iso'))
# obs2 =mgr.weather_at_place('London')
# print(obs2.location)
# from pytz import timezone
#
# # print(obs2.reception_time(timeformat='iso'))
# from geopy import geocoders
# from tzwhere.tzwhere import tzwhere
# g = geocoders.GoogleV3('YAIR GAT')
# tz = tzwhere()
# locationList = ["Sackville, Canada", "Romania", "Mannheim, Germany", "New Delhi, India", "Trier, Germany", "Basel, Switzerland", "Bruxelles/Brussel, Belgium"]
#
# for location in locationList:
#     place, (lat, lng) = g.geocode(location)
#     timeZoneStr = tz.tzNameAt(lat, lng)
#     timeZoneObj = timezone(timeZoneStr)
timeZ_Kl = pytz.timezone('Asia/Kolkata')
dt_Kl = datetime.now(timeZ_Kl)

print(dt_Kl.time())