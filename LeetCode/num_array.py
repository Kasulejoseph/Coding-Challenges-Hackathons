class NumArray:

    def __init__(self, nums: list()):
        self.nums_list = nums

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for k in range(i, j+1):
            print(self.nums_list[k])
            sum += self.nums_list[k]
        return sum

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)
print(param_1)