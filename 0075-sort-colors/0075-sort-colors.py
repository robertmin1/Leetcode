class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, length = 1, len(nums)
        while curr < length:
            for num in range(length-1):
                if nums[num] > nums[num+1]:
                    temp = nums[num+1]
                    nums[num+1] = nums[num]
                    nums[num] = temp
            curr+=1
        
        return nums