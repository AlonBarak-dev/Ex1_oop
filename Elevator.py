

class Elevator:

    def __init__(self,id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime,currentDirection, listOfCalls,currentFloor):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self._currentDirection = currentDirection
        self._listOfCalls = listOfCalls
        self.currentFloor = currentFloor

    def __str__(self):
        string = "id = ", self._id, " speed: ", self._speed, " minFloor: " , self._minFloor, " maxFloor: ", self._maxFloor," closeTime: ", self._closeTime, " openTime: ", self._openTime, "startTime: ", self._startTime, " stopTime: ", self._stopTime," currentDirection: ", self._currentDirection, " calls: ", self._listOfCalls, " currentFloor: ", self.currentFloor
        return string



