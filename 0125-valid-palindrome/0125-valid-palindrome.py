class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for letter in s:
            if letter.isalnum():
                palindrome+=letter.lower()
    
        return palindrome == ''.join(reversed(palindrome))