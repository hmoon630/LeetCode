# https://leetcode.com/problems/string-to-integer-atoi
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        regex = "[\-+]?\d+"
        result = re.match(regex, s.strip())
        if result:
            num = int(float(result.group()))
            if num >= 2 ** 31 - 1 or num <= -2 ** 31:
                return 2 ** 31 - 1 if num > 0 else -2 ** 31
            return num
        else:
            return 0
        

cases = ["42", "    -42", "4193 with words", "words with 009821", "-91283472332"]
for case in cases:
    print(Solution().myAtoi(case))