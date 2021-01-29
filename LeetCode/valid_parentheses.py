class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'{': '}', '(': ')', '[': ']'}
        if s == "":
            return False

        for item in s:
            if item in parentheses:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                print(stack, item)
                if parentheses[stack[-1]] == item:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

print(Solution().isValid("(])"))