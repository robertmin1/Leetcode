class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        def helper(pro, unpro):
            if not unpro:
                return [pro]
            
            res = []
            res.extend(helper(pro+ [unpro[0]], unpro[1:]))
            res.extend(helper(pro, unpro[1:]))

            return res

        return helper([], nums)