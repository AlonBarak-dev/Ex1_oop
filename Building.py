import json

class Building:

    def __init__(self, minFloor, maxFloor, elevators, numberOfElevators):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevators = elevators
        self.numberOfElevators = numberOfElevators

    def __str__(self):
        elevStr = ()
        for i in self._elevators:
            elevStr.__add__(i.__str__())

        string = "minFloor: ", self._minFloor, " maxFloor: ", self._maxFloor, " numberOfElevators: ", self.numberOfElevators
        print(string , elevStr )