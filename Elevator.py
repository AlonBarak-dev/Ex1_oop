

class Elevator:

    def __init__(self,data):
        self._id = data["id"]
        self._speed = data["speed"]
        self._minFloor = data["minFloor"]
        self._maxFloor = data["maxFloor"]
        self._closeTime = data["closeTime"]
        self._openTime = data["openTime"]
        self._startTime = data["startTime"]
        self._stopTime = data["stopTime"]
        self._currentDirection = 0  # 0 -> still, 1 -> down, 2 -> up
        self._listOfCalls = []
        self.currentFloor = 0

    """
    def __str__(self):
        string = "id = ", self._id, " speed: ", self._speed, " minFloor: " , self._minFloor, " maxFloor: ", self._maxFloor," closeTime: ", self._closeTime, " openTime: ", self._openTime, "startTime: ", self._startTime, " stopTime: ", self._stopTime," currentDirection: ", self._currentDirection, " calls: ", self._listOfCalls, " currentFloor: ", self.currentFloor
        return string
    """



