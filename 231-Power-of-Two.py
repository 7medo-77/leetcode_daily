class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # if n == 0 or n < 0:
        #     return False
        # while (n > 0):
        #     n /= 2
        #     print(n)
        #     if (n % 2 != 0 and n > 1):
        #         return False
 
        if n == 0 or n < 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n / 2)
        # return True

