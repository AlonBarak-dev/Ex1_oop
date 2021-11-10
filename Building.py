import json

from Elevator import Elevator


class Building:

    def __init__(self, filename):
        f = open(filename)
        data = json.load(f)
        self._minFloor = data['_minFloor']
        self._maxFloor = data['_maxFloor']
        self._elevators = []
        for elev in data["_elevators"]:
            elevator = Elevator(elev)
            self._elevators.append(elevator)
        self._numberOfElevators = len(self._elevators)


    """
    def __str__(self):
        elevStr = ()
        for i in self._elevators:
            elevStr.__add__(i.__str__())

        string = "minFloor: ", self._minFloor, " maxFloor: ", self._maxFloor, " numberOfElevators: ", self.numberOfElevators
        print(string , elevStr )
    """