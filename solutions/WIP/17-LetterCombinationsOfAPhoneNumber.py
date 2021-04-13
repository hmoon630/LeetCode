# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from itertools import permutations, combinations

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        num_2 = permutations(num_dic["2"])
        num_3 = permutations(num_dic["7"])

        for i in num_2:
            for j in num_3:
                result.update(set(map(lambda x: "".join(x), zip(i, j))))
        return list(result)


cases = ["2"]
for case in cases:
    print(Solution().letterCombinations(case))
