# https://leetcode.com/problems/set-matrix-zeroes/
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution(object):
    def setZeroes(self, matrix):
        # optimal: O(n*m) no extra space
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        # check if first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        # check if first col contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        # Mark the first row and first column for setting zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Set the cells to zero based on marks in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the first row to zero if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        # Set the first column to zero if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


obj = Solution()
matrix = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
obj.setZeroes(matrix)
print(matrix)

