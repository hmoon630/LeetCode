# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


cases = [[[4, 5, 6, 7, 0, 1, 2], 0], [[4, 5, 6, 7, 0, 1, 2], 3]]

for case in cases:
    print(Solution().search(*case))