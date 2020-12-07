class Solution:
    def twoSum(self, nums: list(), target: int) -> list():
        for i in range(len(nums)):
            y = target - nums[i]
            for j in range(i+1, len(nums)):
                print(nums[i], y, nums[j], j)
                if nums[j] == y:
                    return [i, j]

print(Solution().twoSum([3,3], 6))