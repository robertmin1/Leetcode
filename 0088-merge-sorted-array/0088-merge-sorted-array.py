class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m
        for num in range(n):
            nums1[start] = nums2[num]
            start+=1
        nums1.sort()
        