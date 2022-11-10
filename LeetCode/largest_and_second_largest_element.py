"""
Finding the largest element in an array is extremely common. Here is how you can simply do it:
"""
def largestNumber(nums):
    largest_number = nums[0]
    for num in nums:
        if num > largest_number:
            largest_number = num
    print(largest_number)
    return largest_number

def secondMaximum(nums):
    first_max = max(nums[0], nums[1])
    second_max = min(nums[0], nums[1])
    for i in range(2, len(nums), 1):
        if nums[i] > first_max:
            second_max = first_max
            first_max = nums[i]
        elif nums[i] > second_max:
            second_max = nums[i]
    print("=====>>>", first_max, second_max)


largestNumber([5, 7, 8, 9, -1, 3, 19, -28])
secondMaximum([85, 7, 18, 9, -1, 3, 19, -28])