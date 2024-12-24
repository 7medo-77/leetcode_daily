class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deltaArray = [0 for i in range(len(temperatures))]
        tempStack = []

        for index, value in enumerate(temperatures):
            # valueTuple = (value, index)
            # print(tempStack)
            if len(tempStack) != 0 and value > temperatures[tempStack[-1]]:
                while len(tempStack) > 0 and value > temperatures[tempStack[-1]]:
                    deltaArray[tempStack[-1]] = index - tempStack[-1]
                    tempStack.pop()
            tempStack.append(index)

        return deltaArray