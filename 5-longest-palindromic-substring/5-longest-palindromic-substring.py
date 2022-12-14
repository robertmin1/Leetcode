class Solution:
    def longestPalindrome(self, s: str) -> str:
        hlen = 0
        lstr = ""

        for i in range(len(s)):
            l,r = i,i
            #odd
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)> hlen:
                    hlen = r-l+1
                    lstr = s[l:r+1]
                l-=1
                r+=1
            #even
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)> hlen:
                    hlen = r-l+1
                    lstr = s[l:r+1]
                l-=1
                r+=1
        return lstr