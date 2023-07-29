
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0 for i in range(n)] for x in range(n)]
        count = 1
        cols_start, cols_end = 0, n
        rows_start, rows_end = 0, n
        
        while cols_end > cols_start and rows_end > rows_start:
            
            # Fill the top row
            for i in range(cols_start, cols_end):
                ans[cols_start][i] = count
                count += 1
            cols_start += 1
            
            # Fill the rightmost column
            for j in range(cols_start, cols_end):
                ans[j][cols_end-1] =  count
                count += 1  
        
            rows_start += 1
            
            # Fill the bottom row
            if rows_start <= rows_end:
                for i in range(rows_end-1, rows_start-1, -1):
                    ans[rows_end-1][i-1] =  count
                    count += 1
            
            # Fill the leftmost column
            if cols_start <= cols_end:
                for j in range(rows_end-2, rows_start-1, -1):
                    ans[j][rows_start-1] = count 
                    count += 1
            
            rows_end -= 1
            cols_end -= 1
            
            
        return ans
                



print(Solution().generateMatrix(1))