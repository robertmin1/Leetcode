class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, True), self.search(nums, target, False)]
    def search(self, nums, target:int, first:bool):
        ans = -1
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if target > nums[mid]:
                start = mid+1
            elif target < nums[mid]:
                end = mid-1
            else:
                ans = mid
                if first:
                    end = mid-1
                else:
                    start = mid+1
        return ans