class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        res = dict(res)
        for num in nums:
            if num in res:
                res[num] +=1
            else:
                res[num] = 1
        return max(res, key=res.get)
            