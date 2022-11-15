"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

"""
import math
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return max(nums)
        thirdMax = -math.inf
        firstMax = -math.inf
        secondMax = -math.inf
        
        for i in range(len(nums)):
            if nums[i] > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = nums[i]
            elif nums[i] > secondMax and nums[i] < firstMax:
                thirdMax = secondMax
                secondMax  = nums[i]
                
            elif nums[i] > thirdMax and nums[i] < secondMax or secondMax == thirdMax:
                thirdMax = nums[i]
        if thirdMax == -math.inf:
            return firstMax
        else:
            return thirdMax

answer = Solution()
print(answer.thirdMax([5,5,5,5,10,5,10,10,10,20]))
