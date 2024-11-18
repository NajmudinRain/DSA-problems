# arr is sorted in row and col wise manner
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False

obj = Solution()
matrix= [
    [10, 20 , 30, 40],
    [11, 21, 31, 41],
    [15, 25, 35, 45],
    [18, 28, 38, 48]
]
print(obj.searchMatrix(matrix, 18))

