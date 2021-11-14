import csv
import Building
from Elevator import Elevator


class Calls:

    def __init__(self, data):
        self.text = data[0]
        self.time = float(data[1])
        self.source = int(data[2])
        self.destination = int(data[3])
        self.state = int(data[4])
        self.allocateTo = -1  # default value
        if self.source > self.destination:
            self.direction = 1      # down
        else:
            self.direction = 2      # up


    def allocate(self, building : Building, numOfFloors):
        range = int(numOfFloors / (building.numberOfElevators))
        roadLength = abs(self.source - self.destination)
        elevatorId = int(roadLength / range)
        if elevatorId >= building.numberOfElevators:
            elevatorId = building.numberOfElevators - 1
        self.allocateTo = elevatorId
        return elevatorId





