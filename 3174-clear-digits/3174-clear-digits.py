class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if not stack and i.isdigit():
                stack.append()
            if stack and i.isdigit() and stack[-1].isalpha():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

        