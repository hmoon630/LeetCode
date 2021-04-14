# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"[": "]", "{": "}", "(": ")"}

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                try:
                    if c != parentheses[stack.pop()]:
                        return False
                except IndexError:
                    return False

        if stack:
            return False
        else:
            return True


cases = ["()", "()[]{}", "(]", "([)]", "("]

for case in cases:
    print(Solution().isValid(case))