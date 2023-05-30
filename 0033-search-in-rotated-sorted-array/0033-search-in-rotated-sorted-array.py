class Solution:
    def search(self, nums: List[int], target: int) -> int:
        peaknum = self.peak(nums)
        
        if peaknum == None:
            return(self.binary(nums, 0, len(nums)-1, target))
        elif nums[peaknum] == target:
            return peaknum
        
        return self.binary(nums, 0, peaknum-1,target) if target >= nums[0] else self.binary(nums,peaknum+1,len(nums)-1,target)
        
    
    def binary(self, nums, start, end,target):
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        return -1
    
    def peak(self, nums) -> int:
        start = 0
        end = len(nums) -1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if mid < end and nums[mid] > nums[mid+1]:
                return mid
            elif mid > start and nums[mid] < nums[mid-1]: 
                return mid-1
            
            if nums[mid] >= nums[start]:
                start =  mid+1
            else:
                end = mid-1