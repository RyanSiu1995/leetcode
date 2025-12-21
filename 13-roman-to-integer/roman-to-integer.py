class Solution:
    _map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    def romanToInt(self, s: str) -> int:
        stack = []
        out = 0
        for c in s:
            val = self._map[c]
            if not stack or stack[-1] >= val:
                stack.append(val)
            else:
                cur = val - stack.pop() 
                out += cur + sum(stack)
                stack = []
        return out + sum(stack)

            