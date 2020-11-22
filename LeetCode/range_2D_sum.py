class NumMatrix:

    def __init__(self, matrix: list()):
        self.data = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sum += self.data[i][j]
        return sum


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
param_1 = obj.sumRegion(1, 2, 2, 4)
print(param_1)