class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                self.swap(nums, i, correct)
            else:
                i += 1

        return self.check(nums)

    def swap(self, nums:list, first:int, second:int) -> None:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp

    def check(self, nums:list) -> int:
        for num in range(1, len(nums)+ 1):
            if num != nums[num - 1]:
                return nums[num-1]