# https://leetcode.com/problems/regular-expression-matching

import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.match(p, s)
        if result:
            return result.group() == s
        else:
            return False


s = "aa"
p = "a"
print(Solution().isMatch(s, p))
