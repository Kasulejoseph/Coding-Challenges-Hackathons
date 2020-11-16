class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        if rec2[0] <= rec1[0]:
            x_difference = rec2[-2] - rec1[0]
            y_difference = rec2[-1] - rec1[1]
            print(x_difference, y_difference)
            return x_difference > 0 and y_difference > 0
        xt_difference = rec1[-2] - rec2[0]
        yt_difference = rec1[-1] - rec2[1]
        print(rec1[-2], rec2[0])
        print(xt_difference, yt_difference)
        if xt_difference > 0 and yt_difference > 0:
            return True
        return False

print(Solution().isRectangleOverlap([-9,6,-3,10], [-8,-10,-5,-4]))