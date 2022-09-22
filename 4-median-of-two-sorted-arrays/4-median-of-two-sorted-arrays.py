class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for value in nums2:nums1.append(value)
        nums1 = sorted(nums1)
        if len(nums1)%2 == 0:
            left = 0
            right = len(nums1)-1
            while left != right-1:
                left+=1
                right-=1
            return((nums1[left]+nums1[right])/2)
        else:
            left = 0
            right = len(nums1)-1
            while left != right:
                left+=1
                right-=1
            return(nums1[left])