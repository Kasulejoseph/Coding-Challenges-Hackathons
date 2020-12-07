class Solution:
    # def __init__(self):
    #     # new_board =

    def neighbors(self, value, board, ones):
        dx = [-1, 0, 1]
        dy = [1, 0, -1]

        for x in dx:
            for y in dy:
                print((x, y), board[x][y])

                if board[x][y] == 1:
                    print("yeessss=========>", ones)
                    ones += 1
        print(ones)
        if ones > 3 and value == 1:
            return 0
        elif 1 < ones < 3 and value == 1:
            return 1
        elif ones < 2 and value == 1:
            return 0
        elif ones == 3 and value == 0:
            return 1
        else:
            return 0


    def gameOfLife(self, board: list()) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = [[0]* len(board[0]) for _ in range(len(board))]
        print(new_board)
        for i in range(len(board[0])):
            for j in range(len(board[i])):
                new_board[i][j] = self.neighbors(board[i][j], board, 0)
        return new_board



        # for j in range(len(board)):
        #     for i in range(len(board[j])):
        #         cell_count = len(board[j])
        #         if i == 0 and j == 0:
        #             neighbor_cell = [board[j][i+1], board[j+1][i:i+2]]
        #             # print(neighbor_cell)
        #         elif i == cell_count-1 and j == 0:
        #             neighbor_cell4 = [board[j][i - 1], board[j + 1][i-1:i+2]]
        #         elif i == 0 and j == len(board) - 1:
        #             neighbor_cell5 = [board[j][i + 1], board[j - 1][i:i+2]]
        #             # sum(neighbor_cell)
        #         elif i == cell_count-1 and j == len(board) - 1:
        #             neighbor_cell6 = [board[j][i - 1], board[j - 1][i-1:i+2]]
        #             print("=====>", neighbor_cell6)
        #             return
        #             # sum(neighbor_cell)
        #         #
        #         else:
        #             if (j == 0):
        #                 neighbor_cell2 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]
        #
        #             # if not(j == 0 or j == -1):
        #                 # neighbor_cell2 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]
        #                 # print(board[j][i])
        #             # else:
        #                 # neighbor_cell3 = [board[j][i-1],  board[j][i+1], board[j-1][i-1:i+2], board[j+1][i-1:i+2]]
        #                 # return neighbor_cell2



print(Solution().gameOfLife([[0,1,0],[1,0,1],[0,0,1]]))