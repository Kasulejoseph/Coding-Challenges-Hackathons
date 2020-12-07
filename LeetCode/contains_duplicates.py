
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        if nums == [] or len(nums) == 1:
            return False
        sorted_array = sorted(nums)
        sorted_array.append(sorted_array[-1]+1)
        for i in range(len(nums)):
            if sorted_array[i] == sorted_array[i+1]:
                return True
        return False


print(Solution().containsDuplicate([3, 1]))