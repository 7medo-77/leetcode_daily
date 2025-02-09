class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedArray = sorted(list(zip(position, speed)), key=lambda tuple: tuple[0], reverse=True)
        fleetStack = []

        for index, tupleElement in enumerate(positionSpeedArray):
            carPosition = tupleElement[0]
            carSpeed = tupleElement[1]
            carArrivalTime = (target - carPosition) / carSpeed

            if not fleetStack or carArrivalTime > fleetStack[-1]:
                fleetStack.append(carArrivalTime)

        return len(fleetStack)