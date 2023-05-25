class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for per in accounts:
            curr = 0
            for m in per:
                curr+=m
            if curr > res:
                res = curr
        return res
                