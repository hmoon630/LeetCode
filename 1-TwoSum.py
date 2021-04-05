# https://leetcode.com/problems/two-sum/
from typing import List
from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combs = list(combinations(nums, 2))

        for comb in combs:
            if sum(comb) == target:
                return [nums.index(comb[0]), nums.index(comb[1], nums.index(comb[0]) + 1)]

print(Solution().twoSum(nums = [3,3], target = 6))
