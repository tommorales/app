__author__ = 'tmorales'

from model import Model

class Proxy:

    def __init__(self):
        self.__model = Model()

    def __getattr__(self, item):
        return getattr(self.__model, item)