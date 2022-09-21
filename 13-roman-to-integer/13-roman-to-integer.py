class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
 
        
        convert = {"IV": "IIII", "IX": "IIIIV", "XL":"XXXX", "XC":"LXXXX", "CD": "CCCC", "CM": "DCCCC"}
        
        for i,j in convert.items():
            s = s.replace(i,j)
        
        return sum([values[i] for i in s])