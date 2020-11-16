class Solution:
    def generate(self, numRows: int) -> list():
        if numRows == 0:
            return []
        first_row = [1]
        output = [0] * numRows
        current_row = [1] * numRows
        output[0] = first_row
        for i in range(numRows):
            sub_list = current_row[:i]
            output[i - 1] = sub_list
            if i > 1:
                # print(currentRow)
                # currentRow[:i] = secondRow  n = nt + nt-1
                #      [1],
                #     [1,1], > 0 + 1 > 1
                #    [1,2,1], > 0 + 1 = 1, 1 + 2 = 2
                #   [1,3,3,1], > 0+ 1 = 1, 1+ 2 = 2, 2+ 3 = 3
                # [1,4,6,4,1] >
                # print(currentRow)
                for j in range(len(sub_list) - 1):
                    current_row[j+1] = sub_list[j] + sub_list[j + 1]
        output[numRows - 1] = current_row
        print(type(output))
        return output


print(Solution().generate(0))