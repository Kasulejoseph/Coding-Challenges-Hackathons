import math


class Solution:
    def threeSum(self, nums: list()):
        nums_len = len(nums)
        output = list()
        nums.append(math.inf)
        if nums_len == 0 or nums_len == 1 or nums_len == 2:
            return []
        for i in range(nums_len):
            for j in range(0, nums_len):
                c = nums[i]
                a = nums[nums_len -1 - i]
                # if i == nums_len -1:
                #     print("=========>")
                #     a = nums[i]

                sorted_sum = sorted([a, nums[j], c])
                print(">>>>>>", a, nums[j], c, "======>", nums_len -1 - i, j)
                # print(a, nums[j], c, j , i)
                if a + nums[j] == -c and (nums_len -1 - i) != j:
                    # print(">>>>>>", a, nums[j], c, sorted_sum,  "======>", nums_len - 1 - i, j)
                    if sorted_sum not in output:
                        output.append(sorted_sum)
        return output


print(Solution().threeSum([-1,0,1,2,-1,-4]
))

