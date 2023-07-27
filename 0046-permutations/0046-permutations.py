class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper([], nums)

    def helper(self, pro, unpro):
        if not unpro:
            return [pro]
        
        res = []
        for num in range(len(unpro)):
            curr = unpro[num]
            left = unpro[:num]
            right = unpro[num+1:]
            res.extend(self.helper(pro+[curr], left+right))
        
        return res