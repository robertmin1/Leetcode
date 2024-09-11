class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            
            t = t[t.index(char) + 1:]
        return True