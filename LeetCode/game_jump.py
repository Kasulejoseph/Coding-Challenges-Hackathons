class Solution:
    def canJump(self, nums: list()) -> bool:
        max_jump = 0
        i = 0
        while i <= max_jump:
            print(i, max_jump, nums[i])
            if i == len(nums) - 1:
                return True
            max_jump = max(max_jump, (nums[i] + i))
            i += 1
        return False

print(Solution().canJump([2,2,0,1,4]))
