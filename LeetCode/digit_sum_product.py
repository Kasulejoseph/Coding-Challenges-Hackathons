
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumy = 0
        for num in str(n):
            prod *= int(num)
            sumy += int(num)
        results = prod - sumy
        return int(results)

print(Solution().subtractProductAndSum(4421))