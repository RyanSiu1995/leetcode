import copy
import heapq

class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        heap = copy.deepcopy(happiness)
        heap = [ (-1 * i) for i in heap ]
        heapq.heapify(heap)
        out = 0
        for i in range(k):
            while heap:
                kid = -1 * heapq.heappop(heap)
                if kid - i > 0:
                    break
            if kid - i <= 0: continue
            out += kid - i
        return out