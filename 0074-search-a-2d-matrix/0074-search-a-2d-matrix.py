class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            row = 0
            column = len(matrix[0]) - 1

            while row <= len(matrix) - 1 and column >= 0:
                if matrix[row][column] == target:
                    return True


                if matrix[row][column] > target:
                    column -=1
                elif matrix[row][column] < target:
                    row+=1
                else:
                    return False