from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            res[word_sorted].append(word)

        return list(res.values())