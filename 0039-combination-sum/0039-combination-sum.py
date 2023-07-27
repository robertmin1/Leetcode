class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        def helper(pro, target, start):
            if target == 0:
                return [pro]
            
            index = 0
            res = []
            for num in range(start, len(candidates)):
                if candidates[num] <= target:
                    res.extend(helper(pro+[candidates[num]], target-candidates[num], start=num))

            
            return res
        
        return helper([], target,0)