import json

from Calls import Calls
from Elevator import Elevator


class Building:

    def __init__(self, filename):
        f = open(filename)
        data = json.load(f)
        self.minFloor = data['_minFloor']
        self.maxFloor = data['_maxFloor']
        self.elevators = []
        for elev in data["_elevators"]:
            elevator = Elevator(elev)
            self.elevators.append(elevator)
        self.numberOfElevators = len(self.elevators)
        self.calls = []

    def output(self, call : Calls):
        out = ["Elevator call", call.time, call.source, call.destination, call.state]
        elev_number = call.allocate(self)
        out.append(elev_number)
        out.append("Done")