class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vars = []
        def helper():
            
            for pos_row,m in enumerate(matrix):
                   for pos_col,num in enumerate(m):
                    if num == 0:
                        vars.append([pos_row, pos_col])
        helper()
        for var in vars:
            a,b = var[0], var[1]
            for num in range(len(matrix[0])):
                matrix[a][num] = 0
            for num in range(len(matrix)):
                matrix[num][b] = 0
        