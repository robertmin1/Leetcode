digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        return self.helper("", digits)
    def helper(self, pro, unpro):
        if not unpro:
            return [pro]
        
        d = digit_to_letters[unpro[0]]
        res = []
        for num in range(len(d)):
            ch = d[num]

            res.extend(self.helper(pro+ch, unpro[1:]))
        
        return res