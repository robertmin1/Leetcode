class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters=" ,:.@!`#$%^?\"&*()_-+={}[]\/';'"
        for char in characters:
            s = s.replace(char, "")
        s =s.lower()
        return s == ''.join(reversed(s))
