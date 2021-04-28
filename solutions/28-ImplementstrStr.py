# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


cases = [["hello", "ll"], ["aaaaaaaa", "bba"], ["", ""]]

for case in cases:
    print(Solution().strStr(*case))
