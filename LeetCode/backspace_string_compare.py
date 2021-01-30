class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for i in S:
            if i is not "#":
                stack_s.append(i)
            else:
                if len(stack_s) != 0:
                    stack_s.pop()
        for i in T:
            if i is not "#":
                stack_t.append(i)
            else:
                if len(stack_t) != 0:
                    stack_t.pop()
        return stack_s == stack_t