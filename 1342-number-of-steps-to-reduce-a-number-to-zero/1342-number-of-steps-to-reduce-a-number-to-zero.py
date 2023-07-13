class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num, 0)
    
    def helper(self, num:int, count:int) -> int:
        if num == 0:
            return count
        elif num%2 == 0:
            return self.helper(num/2, count=count+1)
        else:
            return self.helper(num-1, count=count+1)