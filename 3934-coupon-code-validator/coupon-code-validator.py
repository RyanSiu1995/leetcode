import heapq
import re

class Solution:
    _lines = [
        "electronics", "grocery", "pharmacy", "restaurant"
    ]

    def __init__(self):
        self.out = {l: [] for l in self._lines}

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        for i in range(len(code)):
            if (
                not isActive[i] or 
                businessLine[i] not in self._lines or
                not code[i] or
                not re.match(r"^\w+$", code[i])
            ):
                continue
            self.out[businessLine[i]].append(code[i])
        out = []
        print(self.out)
        for i in self.out.values():
            out.extend(sorted(i))
        return out