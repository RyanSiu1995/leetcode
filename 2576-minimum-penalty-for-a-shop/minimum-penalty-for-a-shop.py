class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minPen, prefix, out = 0, 0, 0
        for i in range(len(customers)):
            prefix += (-1 if customers[i] == "Y" else 1)
            if prefix < minPen:
                out = i + 1
                minPen = prefix
        return out
