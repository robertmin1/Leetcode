class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            count = 0
            while num:
                count+=1
                num = num//10
            
            if count%2 == 0:
                res+=1
        return res