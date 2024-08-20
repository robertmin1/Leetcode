class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack) , len(needle)
        for num in range(h):
            if (h - num) >= n and haystack[num:num+n] == needle:
                return num
        
        return -1