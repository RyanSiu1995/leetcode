class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        out = ""
        number, counter = None, 0
        for i in self.countAndSay(n - 1):
            if not number or number == i:
                # If it is the same or initial count, increment counter
                number = i
                counter += 1
            else:
                # If different numbers, append and renew the counter
                out += f"{counter}{number}"
                number, counter = i, 1
        # Last append
        out += f"{counter}{number}"
        return out