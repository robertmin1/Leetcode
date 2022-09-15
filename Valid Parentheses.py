class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        opens = []

        for symbol in s:
            if symbol in dic:
                opens.append(symbol)
            elif opens == [] or symbol != dic[opens.pop()]:
                return False
        return opens == []
