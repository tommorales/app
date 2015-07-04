__author__ = 'tmorales'


from model import Model
from view import View

from pprint import pprint

class Controller:

    def __init__(self):
        self.__model = Model()
        self.__view = View()

    def current(self, city):
        url = "http://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city}
        json = self.__model.rest(url, payload)
        self.__view.current(json)

    def forecast_5_day(self, city):
        url = "http://api.openweathermap.org/data/2.5/forecast"
        payload = {"q": city}
        json = self.__model.rest(url, payload)
        self.__view.time_serie_5_day_3_hour(json)

    def weather_stations(self, id=None, rectangularZone=None, geoPoint=None):
        if id is not None:
            url = "http://api.openweathermap.org/data/2.5/station"
            payload = {"id": id}

        if rectangularZone is not None:
            url = "http://api.openweathermap.org/data/2.5/box/station"
            payload = dict(cluster="no", format="json")
            payload.update(rectangularZone)
            pprint(payload)

        if geoPoint is not None:
            url = "http://api.openweathermap.org/data/2.5/station/find"
            payload = geoPoint

        json = self.__model.rest(url, payload)
        self.__view.weather_stations(json)




