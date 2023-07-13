class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters=" ,:.@!`#$%^?\"&*()_-+={}[]\/';'"
        for char in characters:
            s = s.replace(char, "")
        s =s.lower()
        print(s)
        return self.checker(s,0, len(s)-1)
    
    def checker(self, s:str, start:int, end:int) -> bool:
        if start >= end:
            return True
        elif s[start] != s[end]:
            return False
        else:
            return self.checker(s, start=start+1, end=end-1)
        