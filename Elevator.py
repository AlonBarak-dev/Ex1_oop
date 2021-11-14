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
        self.currentDirection = 0  # 0 -> still, 1 -> down, 2 -> up
        self.listOfCalls: Calls = []
        self.listOfTimes = []
        self.time = self.stopTime + self.startTime + self.openTime + self.closeTime + self.speed

    def locate(self, time):
        if len(self.listOfTimes) == 0:
            return 0
        i = 0
        while True:
            if i == len(self.listOfTimes):
                break
            if time >= self.listOfTimes[i]:
                i += 1
        if i == len(self.listOfTimes):
            return self.listOfCalls[i - 1]
        return self.listOfCalls[i]

    def getCall(self, index) -> Calls:
        return self.listOfCalls[index]
