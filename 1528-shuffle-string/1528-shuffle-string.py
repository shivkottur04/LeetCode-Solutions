class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        lst=[0]*len(s)
        for i in range(len(indices)):
            lst[indices[i]]=s[i]
        return "".join(lst)
        