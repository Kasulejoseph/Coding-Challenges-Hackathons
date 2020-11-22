class Solution:
    def gameOfLife(self, board: list()) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for j in range(len(board)):
            for i in range(len(board[j])):
                cell_count = len(board[j])
                if i == 0 and j == 0:
                    neighbor_cell = [board[j][i+1], board[j+1][i:i+2]]
                    # print(neighbor_cell)
                elif i == cell_count-1 and j == 0:
                    neighbor_cell4 = [board[j][i - 1], board[j + 1][i-1:i+2]]
                elif i == 0 and j == len(board) - 1:
                    neighbor_cell5 = [board[j][i + 1], board[j - 1][i:i+2]]
                    # sum(neighbor_cell)
                elif i == cell_count-1 and j == len(board) - 1:
                    neighbor_cell6 = [board[j][i - 1], board[j - 1][i-1:i+2]]
                    print("=====>", neighbor_cell6)
                    return
                    # sum(neighbor_cell)
                #
                else:
                    if (j == 0):
                        neighbor_cell2 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]

                    # if not(j == 0 or j == -1):
                        # neighbor_cell2 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]
                        # print(board[j][i])
                    # else:
                        # neighbor_cell3 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]
                        # return neighbor_cell2



print(Solution().gameOfLife([[0,1,0],[1,0,1],[0,0,1]]))