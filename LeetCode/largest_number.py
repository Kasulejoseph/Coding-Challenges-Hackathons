# Hint: use comparators
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list()) -> str:
        string_array = [str(nums[a]) for a in range(len(nums))]

        def cmp(x, y):
            a_b = x + y
            b_a = y + x
            if a_b > b_a:
                return -1
            if a_b == b_a:
                return 0
            else:
                return 1
            return cmp

        sorted_list = sorted(string_array, key=cmp_to_key(cmp), reverse=False)
        sorted_to_string = ''.join(sorted_list)
        if int(sorted_to_string) == 0:
            return '0'
        return sorted_to_string


print(Solution().largestNumber([0, 1, 0, 0]))
