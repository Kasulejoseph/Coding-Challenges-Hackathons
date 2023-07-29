class Solution:
    ans = []
    def recursive(self, matrix, rows, cols, i):
        print(i, rows, cols)
        if i >=rows or i>=cols:
            # print(i, rows)
            return 

        # first row
        
        for p in range(i, cols):
            # print("+_++_+++", matrix[i])
            self.ans.append(matrix[i][p])
            # print(matrix[i][p])
            
        # last column
        for q in range(i+1, rows):
            # print(">>",matrix[q][cols-1])
            self.ans.append(matrix[q][cols-1])
            # print(matrix[q][cols-1])
            
        # last row
        
        for p in range(cols-1, i, -1):
            # print(">>>>>>>>>>>",matrix[rows-1], matrix[rows-1][p-1], i, rows-1)
            # if not (matrix[rows-1][p-1] in self.ans):
            if i < rows-1:
                self.ans.append(matrix[rows-1][p-1])
            # print(matrix[rows-1][p-1])
            
        # first column
        print("@@@@", i, rows, cols)
        for q in range(rows-2, i, -1):
            print("++++++++", matrix[q], q, i, matrix[q][i])
            # if not (matrix[q][i] in self.ans):
            if i < cols-1:
                self.ans.append(matrix[q][i])
            # print(matrix[q][i])
        
        self.recursive(matrix, rows-1, cols-1, i+1)
        print(self.ans)
        
        
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        self.ans = []
        if cols < 2:
            print("hehehe", cols)
            self.ans = [ matrix[a][0] for a in range(len(matrix)) ]
            return self.ans
        self.recursive(matrix, rows, cols, 0)
        return self.ans

        
        
        

print(Solution().spiralOrder([
        [2,3,4],
        [5,6,7],
        [8,9,10],
        [11,12,13],
        [14,15,16]
        ]))