class Solution:
    def removeDuplicates(self, s: str) -> str:
        lst=[]
        for i in s:
            if len(lst)>0 and lst[-1]==i:
                lst.pop()
            else:
                lst.append(i)
        return "".join(lst)