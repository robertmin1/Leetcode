class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        last = "I"
        
        for numerical in s[::-1]:
            if values[numerical] < values[last]:
                sum-=values[numerical]
            else:
                sum+=values[numerical]
            last = numerical
        return sum
