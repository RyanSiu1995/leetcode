class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c, s, out = sorted(capacity, reverse=True), sum(apple), 0
        s = sum(apple)
        for i in c:
            if s <= 0:
                break
            s -= i
            out += 1
        return out