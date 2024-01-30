class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square(n:int) -> int:
            ans = 0
            
            while n > 0:
                rem = n % 10
                ans+= rem * rem
                n = int(n / 10)
            
            return ans
        
        f, s = square(square(n)), square(n)
        
        
        while f != s:
            f = square(square(f))
            s = square(s)
            
            if f == 1:return True
            if f == s:return False
        
        return True
    

