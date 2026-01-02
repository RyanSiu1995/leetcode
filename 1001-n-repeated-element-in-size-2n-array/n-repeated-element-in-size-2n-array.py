from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i, v in Counter(nums).items():
            if v == len(nums) // 2:
                return i