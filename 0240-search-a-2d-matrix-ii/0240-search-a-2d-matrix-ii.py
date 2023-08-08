class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            for num in l:
                if num == target:
                    return True
    
        
        return False