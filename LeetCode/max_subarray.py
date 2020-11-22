class Solution:
    def maxSubArray(self, nums: list()) -> int:
        max_array = [0]
        array_1 = []
        if len(nums) == 1:
            return nums[0]
        for k in range(len(nums)):
            for j in range(k + 1, len(nums)+1):
                sub_list = nums[k:j]
                sub_sum = sum(sub_list)
                array_1.append(sub_sum)
                if max_array[0] == 0 and k == 0:
                    max_array[0] = sub_list[0]


                if array_1[len(array_1) - 1] > sum(max_array):
                    print(array_1, "====>", max_array)
                    max_array[0] = array_1[-1]
                    print(array_1, "<<<<<<<<<<====>", max_array[0])
        print("tyuytyuyt", max_array)
        return max_array[0]


print(Solution().maxSubArray([-1,0,-2]))
