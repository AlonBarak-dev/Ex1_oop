import csv

class Calls:

    def __init__(self,data):
        self._text = data[0]
        self._time = data[1]
        self._source = data[2]
        self._destination = data[3]
        self._state = data[4]
        self._allocateTo = -1   # default value
        if(self._source > self._destination):
            self._direction = 1
        else:
            self._direction = 2

