class Solution:
    def intToRoman(self, num: int) -> str:
        lists = [[1, "I"], [4, "IV"], [5, "V"], [9, "IX"], 
            [10, "X"], [40, "XL"], [50, "L"], [90, "XC"], [100, "C"], 
            [400,"CD"], [500, "D"], [900,"CM"], [1000,"M"]]
        result = ""
        for values,label in reversed(lists):
            if num // values:
                count = num // values
                result+=label*count
                num = num % values
        
        return result
