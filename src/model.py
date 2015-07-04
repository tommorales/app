__author__ = 'tmorales'


import os
import requests


class Model:

    def rest(self, url, payload):
        try:
            r = requests.get(url, params=payload)
        except requests.exceptions.RequestException, e:
            print "Error", e

        return r.json()