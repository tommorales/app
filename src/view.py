__author__ = 'tmorales'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pprint import pprint

class View:

    def current(self, json):
        pprint(json["main"])

    def time_serie_5_day_3_hour(self, json):
        cityName = json["city"]["name"]
        temp_day = map(lambda i: i["main"]["temp"], json["list"])
        vt = map(lambda i: i["dt_txt"], json["list"])
        pd.DataFrame({"temp_day": np.array(temp_day)-273}, index=vt ).plot(lw=2)
        plt.title(cityName)
        plt.ylabel("C")
        plt.savefig("forecast_5_day_{0}".format(cityName))

    def weather_stations(self, json):
        pprint(json)
