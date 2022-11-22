class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for num in range(len(nums)-1):
            if nums[num] == nums[num+1]:
                return nums[num]