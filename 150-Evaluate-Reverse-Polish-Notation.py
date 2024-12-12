class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        symbolDict = {
            '+': lambda a,b: a + b,
            '-': lambda a,b: a - b,
            '*': lambda a,b: a * b,
            '/': lambda a,b: a / b,
        }

        for index, num in enumerate(tokens):
            try:
                number = int(num)
                numStack.append(num)
            except ValueError:
                numPost = int(numStack.pop())
                numPre = int(numStack.pop())
                # print(numPre, num, numPost)
                res = symbolDict[num](int(numPre), int(numPost)) 
                numStack.append(str(int(res)))
        return int(numStack[0])

        #     if type(int(num)) == 'int' :
        #         number = int(num)
        #         print(type(int(num)))
        #         numStack.append(num)
        #     else:
        #         print(type(int(num)))
        #         print(num)
        #         print(numStack)
        #         numPost = int(numStack.pop())
        #         numPre = int(numStack.pop())
        #         print(numPost, numPre)
        #         res = symbolDict[num](int(numPre), int(numPost)) 
        #         numStack.append(str(int(res)))
        # return numStack[0]