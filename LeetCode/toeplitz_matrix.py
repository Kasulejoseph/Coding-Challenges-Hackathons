from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                if i != 0 and j != 0:
                    previous_diagonal_index = matrix[i-1][j-1]
                    if row[j] != previous_diagonal_index:
                        return False
                        
                    print(row[j], )
        if not False:
            return True
                    
sol = Solution()            
print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))