import Calls


class Elevator:

    def __init__(self, data):
        self.id = data["id"]
        self.speed = data["speed"]
        self.minFloor = data["minFloor"]
        self.maxFloor = data["maxFloor"]
        self.closeTime = data["closeTime"]
        self.openTime = data["openTime"]
        self.startTime = data["startTime"]
        self.stopTime = data["stopTime"]
        self.currentDirection = 0  # 0 -> still, 1 -> down, 2 -> up
        self.listOfCalls: Calls = []

    def locate(self, time):
        if len(self.listOfCalls) == 0:
            return 0
        i = 0
        while time >= self.listOfCalls[i]:
            i += 1

        if i == len(self.listOfCalls):
            return self.listOfCalls[i-1]
        return self.listOfCalls[i]
