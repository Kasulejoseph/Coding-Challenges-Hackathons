class Solution:
    def maxProduct(self, nums: list()) -> int:
        max_prodx = nums[0]
        max_prod = 1
        min_value = 1
        array_len = len(nums)
        prev_value = 0
        prefix_sum = [0 for _ in range(len(nums) + 1)]
        if len(nums) == 1:
            return nums[0]
        for i in range(array_len):
            max_prod = max_prod * nums[i]
            min_value = min_value * nums[array_len - i - 1]
            print("======>", max_prod,min_value )
            max_current = max(max_prod, min_value)
            if max_current > max_prodx:
                max_prodx = max_current
            if max_prod == 0:
                max_prod = 1
            if min_value == 0:
                min_value =  1
        return max_prodx


print(Solution().maxProduct([-1,-2,-3,0]))

# [-2,0,-1]
# [2,-5,-2,-4,3]
# [0, 2]
# [-2,3,-4]
# [-3,0,1,-2]
# [2,3,-2,4]
# p[n+1] = max(p[n-1], p_next)

# p_next = num[i] * p[i]
# p[i] = num[i] * p[i-1]

