import random


class Solution:

    def __init__(self, nums: list()):
        self.num_dict = dict([])
        for i in range(len(nums)):
            if nums[i] in self.num_dict:
                self.num_dict[nums[i]].append(i)
            else:
                self.num_dict[nums[i]] = [i]

    def pick(self, target: int) -> int:
        my_choice = self.num_dict[target]
        if len(my_choice) > 1:
            return random.choice(my_choice)
        return my_choice[0]


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])
param_1 = obj.pick(3)
print(param_1)
