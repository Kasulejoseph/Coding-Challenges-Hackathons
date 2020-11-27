class Solution:
    def maxSubArray(self, nums: list()) -> int:
        current_max = 0
        max_sublist = nums[0]
        for i in range(len(nums)):
            print(current_max, nums[i])
            current_max = max(current_max + nums[i], nums[i])
            if max_sublist < current_max:
                print("yrrrrrrr", max_sublist, )
                max_sublist = current_max

        return max_sublist


print(Solution().maxSubArray([-2, 0, -1]))