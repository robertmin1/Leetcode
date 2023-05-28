class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        temp = sorted(arr)
        ans = arr.index(temp[len(arr) -1])
        return ans