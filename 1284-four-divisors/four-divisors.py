from functools import cache

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        out = 0

        @cache
        def searchSumFourDivisors(num: int) -> int:
            candidate = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    candidate.add(i)
                    candidate.add(num // i)
                    if len(candidate) > 4: return 0
            if len(candidate) == 4:
                return sum(candidate)
            else:
                return 0

        for i in nums:
            out += searchSumFourDivisors(i)
    
        return out