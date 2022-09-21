class Solution:
    def convert(self, s: str, numRows: int) -> str:
        space = 0
        if numRows == 1:
            return s
        result = ""
        algo = (numRows-1)*2
        for num in range(numRows):
            if num == 0 or num == numRows-1:
                curr = num
                while curr < len(s):
                    result+=s[curr]
                    curr+=algo
            else :
                curr = num
                space+=2
                p = algo-space
                while curr< len(s):
                    result+=s[curr]
                    if curr+p< len(s):
                        result+=s[curr+p]
                    curr+=algo
            

        return result
