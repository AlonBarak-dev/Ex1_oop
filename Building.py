import json

from Calls import Calls
from Elevator import Elevator


class Building:

    def __init__(self, filename):
        f = open(filename)
        data = json.load(f)
        self.minFloor = data['_minFloor']
        self.maxFloor = data['_maxFloor']
        elevators = []
        for elev in data["_elevators"]:
            elevator = Elevator(elev)
            elevators.append(elevator)
        self.elevators = sorted(elevators, key= lambda x: x.time)
        self.numberOfElevators = len(self.elevators)
        self.calls = []

    def findMaxRoad(self):
        longest = 0
        for call in self.calls:
            road = abs(call.source - call.destination)
            if road > longest:
                longest = road
        return longest


    def output(self, call : Calls):
        out = ["Elevator call", call.time, call.source, call.destination, call.state]
        road = self.findMaxRoad()
        elev_number = call.allocate(self, road)
        out.append(elev_number)
        out.append("Done")
        return out