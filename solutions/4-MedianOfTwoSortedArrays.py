# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1, nums2)

class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # counting sort
        counter = [0] * (10 ** 6 * 2 + 1)

        for num in nums1 + nums2:
            counter[num] += 1

        counter = counter[10 ** 6 + 1:] + counter[:-(10 ** 6) + 1]
        sorted_nums = list()
        for num, count in enumerate(counter, start=-(10 ** 6)):
            for _ in range(count):
                sorted_nums.append(num)

        if (total := len(sorted_nums)) % 2 == 0:
            return (sorted_nums[total // 2 - 1] + sorted_nums[total // 2]) / 2
        else:
            return sorted_nums[total // 2]

ex1 = [[1, 3], [2, 1]]
ex2 = [[1], [-1]]
ex3 = [[100002], [100000]]
print(Solution().findMedianSortedArrays(*ex3))