from functools import cmp_to_key
import math

class Solution:
    def findLongestChain(self, pairs: list()) -> int:
        # [a, b], [c, d] c > b
        results = list([])
        counts = 0
        if len(pairs) == 1 or len(pairs) == 1:
            return pairs
        sorted_pair = sorted(pairs, key=lambda x: x[1])
        sorted_pair.append([math.inf, math.inf])
        results.append(sorted_pair[0])
        print(sorted_pair)
        for i in range(len(pairs)):
            if results[counts][1] < sorted_pair[i+1][0] and i < len(pairs) - 1:
                counts += 1
                results.append(sorted_pair[i+1])
        print(len(results))
        return results


print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
