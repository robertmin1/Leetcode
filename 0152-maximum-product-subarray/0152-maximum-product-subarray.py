class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Initialize variables to track the maximum and minimum product ending at the current index
        max_product_ending_here = min_product_ending_here = max_product = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # If the current number is negative, we can swap the max and min products
            if num < 0:
                max_product_ending_here, min_product_ending_here = min_product_ending_here, max_product_ending_here
            
            # Update the maximum and minimum products ending at the current index
            max_product_ending_here = max(num, max_product_ending_here * num)
            min_product_ending_here = min(num, min_product_ending_here * num)
            
            # Update the overall maximum product
            max_product = max(max_product, max_product_ending_here)
        
        return max_product

s = Solution()
nums = [2, 3, -2, 4]
print(s.maxProduct(nums))
