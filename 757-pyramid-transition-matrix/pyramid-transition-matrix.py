from collections import defaultdict
from functools import cache, reduce
from itertools import pairwise, product

class Solution:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Mapper for faster evaluation
        mapper = defaultdict(list)
        for i in allowed:
            mapper[i[:2]].append(i[2])

        @cache
        def recur(bot: str) -> bool:
            if len(bot) == 1: return True
            pairs = []
            for i in range(len(bot) - 1):
                pair = bot[i:i+2]
                if mapper[pair]:
                    pairs.append(mapper[pair])
                else:
                    return False
            return reduce(
                lambda x, y: x or y,
                [ recur("".join(i)) for i in product(*pairs)]
            )
        
        return recur(bottom)