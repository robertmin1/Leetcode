class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
        current_sum = 0

        for num in nums:
            # Start a new subarray or extend the current one
            current_sum = max(num, current_sum + num)
            # Update max_sum if the current subarray sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
