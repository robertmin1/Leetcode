class Solution:
    def findMin(self, nums: List[int]) -> int:
        peak = self.Peak(nums)
        
        return nums[peak+1]
            
    def Peak(self, nums) -> int:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if end > mid and nums[mid] > nums[mid+1]:
                return mid
            elif start < mid and nums[mid] < nums[mid-1]:
                return mid-1
            
            if nums[mid] > nums[start]:
                start = mid+1
            else:
                end = mid-1
        
        return -1
    