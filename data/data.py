import numpy as np


class Singleton:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Database(Singleton):
    def __init__(self):
        Singleton.__init__(self)

    def get(self):
        return self._data

    def change(self):
        # Just arbitrary experiment of changing the data
        self.load()

    def load(self):
        # For example from csv or binary files using
        # np.genfromtxt or np.fromfile
        self._data = np.random.randint(0, 10, (3, 3))