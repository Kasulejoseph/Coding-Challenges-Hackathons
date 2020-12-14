import math
class Solution:
    def __init__(self):
        self.digit_sum = 0

    def digit_recursive(self, n):
        num_array = [int(i) * int(i) for i in str(n)]
        return sum(num_array)

    def isHappy(self, n: int) -> bool:
        # store results in dict for easy access all_num = dict
        # turn number to list of individual digits
        # for digit in number array, square the sum of the digits
        # if sum in number dict
        # return false
        # if sum  == 1 return True
        num_dict = dict()
        digit_sum = self.digit_recursive(n)
        count = 0
        if digit_sum == 1:
            return True

        while digit_sum != 1:
            num_dict[digit_sum] = count
            sumxy = self.digit_recursive(digit_sum)
            digit_sum = sumxy
            if digit_sum in num_dict:
                return False
            if sumxy == 1:
                return True
            count += 1


print(Solution().isHappy(10))
