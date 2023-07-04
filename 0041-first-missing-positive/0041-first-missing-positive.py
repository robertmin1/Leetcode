class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            
            if correct >= len(nums) or correct < 0:
                i += 1
            elif nums[i] != nums[correct]:
                self.swap(nums, i, correct)
            else:
                i += 1
        print(nums)
        return self.duplicate(nums)
                
                
    def swap(self, nums: list[int], first:int, second:int) -> None:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
        
    def duplicate(self, nums):
        for num in range(1, len(nums) + 1):
            if num != nums[num - 1]:
                return num
        
        return num + 1