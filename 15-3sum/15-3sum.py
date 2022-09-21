class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return([])
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            lower = i+1
            upper = len(nums)-1
            
            while lower!=upper:
                s = nums[i]+nums[lower]+nums[upper]
                
                if s == 0:
                    result.append(tuple([nums[i],nums[lower],nums[upper]]))
                    
                if s<=0:
                    lower+=1
                    while nums[lower] == nums[lower-1] and lower<upper:
                        lower+=1
                else:
                    upper-=1
        return(result)