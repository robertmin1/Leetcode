class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i]
            if correct >= len(nums):
                i += 1
            elif nums[i] != nums[correct]:
                self.swap(nums, i, correct)
            else:
                i += 1

        return self.check(nums)

    def swap(self, nums:list, first:int, second:int) -> None:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp

    def check(self, nums:list) -> int:
        for num in range(len(nums)):
            if num != nums[num]:
                return num
        return len(nums)