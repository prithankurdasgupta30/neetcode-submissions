class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        x = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in x:
                if stack and stack[-1] == x[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        