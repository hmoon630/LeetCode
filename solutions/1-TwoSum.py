# https://leetcode.com/problems/two-sum/
from typing import List
from itertools import combinations

# Brute Force
class SolutionOld:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combs = list(combinations(nums, 2))

        for comb in combs:
            if sum(comb) == target:
                return [nums.index(comb[0]), nums.index(comb[1], nums.index(comb[0]) + 1)]

# Hash Map
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        dic = dict([(num, index) for index, num in enumerate(nums)])

        for index, num in enumerate(nums):
            if target - num in dic and index != dic[target - num]:
                return [index, dic[target - num]]

print(Solution().twoSum(nums = [3, 3], target = 6))
