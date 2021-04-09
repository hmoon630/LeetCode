# https://leetcode.com/problems/container-with-most-water/
from typing import List

# time out
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        for i1, h1 in enumerate(height):
            for i2, h2 in enumerate(height):
                if i1 == i2:
                    continue
                w = abs(i1 - i2)
                h = min(h1, h2)

                max_ = max(max_, w * h)
        return max_


# answer 49, 1, 16, 2
cases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1]]

for case in cases:
    print(Solution().maxArea(case))
