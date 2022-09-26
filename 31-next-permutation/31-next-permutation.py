class Solution:  
    def nextPermutation(self, nums):
        n = len(nums)
        i = n-1

        while i >= 1 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return 

        for k in range(n-1, i-1, -1):
            if nums[k] > nums[i-1]:
                nums[k], nums[i-1] = nums[i-1], nums[k]
                break

        nums[i:] = nums[i:][::-1]

        return nums