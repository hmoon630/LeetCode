# https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i, c in enumerate(s):
            if roman_dict[s[i - 1]] < roman_dict[c] and i != 0:
                num += roman_dict[c] - roman_dict[s[i - 1]] * 2
            else:
                num += roman_dict[c]
        return num

cases = ["MCMXCIV"]
for case in cases:
    print(Solution().romanToInt(case))
