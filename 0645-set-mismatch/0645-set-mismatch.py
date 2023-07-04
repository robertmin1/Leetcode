class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            
            if nums[i] != nums[correct]:
                self.swap(nums, i, correct)
            else:
                i += 1
        return self.get_duplicate(nums)
        
    def swap(self, nums: list[int], first:int, second:int) -> None:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
    
    def get_duplicate(self, nums: list[int]) -> list[int]:
            res = []
            
            for num in range(1, len(nums) + 1):
                if num != nums[num - 1]:
                    res.append(nums[num - 1])
                    res.append(num)

                    return res