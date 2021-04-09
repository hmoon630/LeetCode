# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs:
            while prefix:
                try:
                    while prefix != s[: len(prefix)]:
                        prefix = prefix[:-1]
                    break
                except:
                    prefix = prefix[:-1]
        return prefix


cases = [["flower", "flow", "flight"]]

for case in cases:
    print(Solution().longestCommonPrefix(case))
