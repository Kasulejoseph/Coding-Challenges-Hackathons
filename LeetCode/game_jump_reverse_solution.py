class Solution:
    def canJump(self, nums: list()) -> bool:
        last_element_index = len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            print(last_element_index, nums[i], i)
            if (i + nums[i]) >= last_element_index:
                last_element_index = i
            i -= 1
        return last_element_index == 0



print(Solution().canJump([1,0,1,1,4]))