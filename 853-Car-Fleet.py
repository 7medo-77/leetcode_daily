class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedArray = sorted(list(zip(position, speed)), key=lambda tuple: tuple[0])
        fleetStack = []
        fleetStack.append(positionSpeedArray[-1])

        for index, tupleElement in enumerate(positionSpeedArray[:-1][::-1]):
            carPosition = tupleElement[0]
            carSpeed = tupleElement[1]
            carArrivalTime = (target - carPosition) / carSpeed

            topStackPosition = fleetStack[-1][0]
            topStackSpeed = fleetStack[-1][1]
            topStackArrivalTime = (target - topStackPosition) / topStackSpeed

            if (carArrivalTime <= topStackArrivalTime):
                if (carSpeed <= topStackSpeed):
                    fleetStack.pop()
                    fleetStack.append(tupleElement)
            else:
                fleetStack.append(tupleElement)
        print(fleetStack)
        return len(fleetStack)
