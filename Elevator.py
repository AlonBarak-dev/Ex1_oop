import Calls


class Elevator:

    def __init__(self, data):
        self.id = data["_id"]
        self.speed = data["_speed"]
        self.minFloor = data["_minFloor"]
        self.maxFloor = data["_maxFloor"]
        self.closeTime = data["_closeTime"]
        self.openTime = data["_openTime"]
        self.startTime = data["_startTime"]
        self.stopTime = data["_stopTime"]
        self.listOfCalls: Calls = []
        self.time = self.stopTime + self.startTime + self.openTime + self.closeTime - self.speed

    def getCall(self, index) -> Calls:
        return self.listOfCalls[index]
