import csv
from Building import Building
from Elevator import Elevator


class Calls:

    def __init__(self, data):
        self.text = data[0]
        self.time = data[1]
        self.source = data[2]
        self.destination = data[3]
        self.state = data[4]
        self.allocateTo = -1  # default value
        if self.source > self.destination:
            self.direction = 1
        else:
            self.direction = 2


    def timeCalc(self, elev : Elevator):
        estdCall: Calls = elev.locate(self.time)
        lstSrc = estdCall.source
        lstTime = estdCall.time
        timeDiff = abs(lstTime - self.time)
        position = lstSrc + timeDiff/elev.speed
        distToSrc = abs(position - self.source)
        distToDst = abs(self.source - self.destination)
        timeToSrc = elev.openTime + elev.closeTime + elev.startTime + elev.stopTime + distToSrc/elev.speed
        timeToDst = elev.openTime + elev.closeTime + elev.startTime + elev.stopTime + distToDst/elev.speed
        return timeToSrc + timeToDst

    def bestTime(self, elev : Elevator, building : Building):
        time = 10000
        elevId = -1
        for e in building.elevators:
            currTime = self.timeCalc(elev)
            if currTime <= time:
                time = currTime
                elevId = e.id
        if elev.id == elevId:
            return True
        return False

    def bestDist(self,elev : Elevator, building : Building):
        dist = abs(building.minFloor - building.maxFloor)
        elevId = -1
        for e in building.elevators:
            estdCall: Calls = e.locate(self.time)
            lstSrc = estdCall.source
            lstTime = estdCall.time
            timeDiff = abs(lstTime - self.time)
            position = lstSrc + timeDiff / elev.speed
            currDist = abs(position - self.source)
            if currDist <= dist:
                dist = currDist
                elevId = e.id
        if elev.id == elevId:
            return True
        return False

    def sameDicr(self, elev:Elevator):
        if elev.currentDirection == self.direction:
            return True
        return False

    def highestPrior(self,elev:Elevator, building : Building):

        if len(elev.listOfCalls) == 0:
            return True

        #for e in building.elevators:


    def creditCalc(self, elev : Elevator, building : Building):
        credit_counter = 0

        if elev.listOfCalls == 0:
            credit_counter += 1

        if self.bestTime(elev,building):         # TO DO BEST_TIME FUNCTION
            credit_counter += 1

        if self.bestDist(elev,building):         # TO DO BEST_DIST FUNCTION
            credit_counter += 1

        if self.sameDicr(elev):         # TO DO SAME_DICR FUNCTION
            credit_counter += 1
        """
        if self.highestPrior(elev,building):     # TO DO HIGHEST_PRIOR FUNCTION
            credit_counter += 1
        """
        return credit_counter

    def allocate(self, building : Building):
        if (self.source > building.maxFloor) or (self.source < building.minFloor) or (self.destination > building.maxFloor) or (self.destination < building.minFloor):
            return -1

        if len(building.elevators) == 1:
            return building.elevators[0].id

        bestCredit = 0
        elevId = -1
        looper = 0
        choosenLooper = 0
        for elev in building.elevators:
            elevCredit = self.creditCalc(elev,building)
            if elevCredit >= bestCredit:
                bestCredit = elevCredit
                elevId = elev.id
                choosenLooper = looper
            looper += 1
        building.elevators[choosenLooper].listOfCalls.append(self)
        return elevId

