class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for row in range(numRows):
            temp = []
            
            for j in range(row + 1):
                if j == 0 or j == row:
                    temp.append(1)
                else:
                    temp.append(res[row-1][j-1] + res[row-1][j])
            
            res.append(temp)
        
        return res
                