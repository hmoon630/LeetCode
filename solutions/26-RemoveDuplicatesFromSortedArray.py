# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


cases = [[0, 0, 1, 1, 2, 3, 3, 3], [1, 1, 2]]

for case in cases:
    print(Solution().removeDuplicates(case))
