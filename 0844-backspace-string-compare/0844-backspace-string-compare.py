class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            if stack:
                if i=='#':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if i != "#":
                    stack.append(i)
        s="".join(stack)
        stack.clear()
        for i in t:
            if stack:
                if i=='#':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if i != "#":
                    stack.append(i)
        t="".join(stack)
        if s==t:
            return True
        else:
            return False

        