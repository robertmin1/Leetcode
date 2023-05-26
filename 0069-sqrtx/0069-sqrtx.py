class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x//2
        
        if x == 1:
            return 1
        
        while start <= end:
            mid = (start + end )//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid -1
            elif mid*mid < x:
                start = mid + 1

        return end
            