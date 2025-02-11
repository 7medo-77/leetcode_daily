class Solution: 
    def searchMatrix(self, matrix, target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid = right // 2
        if (target < matrix[0][0] or target > matrix[-1][-1]):
            return False
    
        while left <= right:
            mid = (right + left) // 2
            print("left: {}, mid: {}, right: {}".format(left, mid, right))
            if (matrix[mid][0] <= target and matrix[mid][-1] >= target):
                innerLeft = 0
                innerRight = len(matrix[mid])
    
                while innerLeft <= innerRight:
                    innerMid = (innerRight + innerLeft) // 2
                    print("innerLeft: {}, innerMid: {}, innerRight: {}".format(innerLeft, innerMid, innerRight))
                    
                    if matrix[mid][innerMid] > target:
                        innerRight = innerMid - 1
                    elif matrix[mid][innerMid] < target:
                        innerLeft = innerMid + 1
                    elif matrix[mid][innerMid] == target:
                        return True
                return False
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                left = mid + 1
        return False

