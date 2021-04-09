# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        reversed_ = int(f"{x}"[::-1]) if x >= 0 else int('-' + f"{abs(x)}"[::-1])
        if reversed_ >= 2 ** 31 - 1 or reversed_ <= -2 ** 31:
            return 0
        return reversed_

ex1 = 123
ex2 = -123

print(Solution().reverse(ex1))
print(Solution().reverse(ex2))