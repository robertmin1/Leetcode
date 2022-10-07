class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = []
        try:
            while nums:
                res.append(nums.index(target))
                nums[nums.index(target)] = -1
                
        except:
            ValueError
        
        return [res[0],res[-1]] if res != [] else [-1,-1]
