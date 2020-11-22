class NumMatrix:

    def __init__(self, matrix: list()):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)] # dp - dynamic programing
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("====>", self.dp)
                self.dp[i+1][j+1] = matrix[i][j] + self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i][j]
                # yy[0][0] =  matrix[i][j] + self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i][j]
                print(self.dp)
                # return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.dp)
        return self.dp[row2 + 1][col2+1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[-4, -5]])
param_1 = obj.sumRegion(0, 0, 0, 0)
print(param_1)