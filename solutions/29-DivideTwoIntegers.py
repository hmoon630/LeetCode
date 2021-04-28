# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend.__truediv__(divisor))

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -(2 ** 31):
            return -(2 ** 31)

        return result


cases = [[10, 3], [7, -3], [0, 1], [1, 1]]

for case in cases:
    print(Solution().divide(*case))
