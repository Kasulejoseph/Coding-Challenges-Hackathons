class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        if rec1[0] == rec1[-2] or rec2[1] == rec2[-1]:
            return False
        if rec2[0] == rec2[-2] or rec1[1] == rec1[-1]:
            return False
        x_not_overlap = rec1[-2] <= rec2[0] or rec1[0] >= rec2[-2]
        y_not_overlap = rec1[-1] <= rec2[1] or rec1[1] >= rec2[-1]
        return not (x_not_overlap or y_not_overlap)

print(Solution().isRectangleOverlap([-9,6,-3,10], [-8,-10,-5,-4]))