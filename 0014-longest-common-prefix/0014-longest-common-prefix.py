class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=strs[0]
        b=strs[-1]
        i=0
        lst=[]
        while i<len(a) and i<len(b):
            if a[i]==b[i]:
                lst.append(a[i])
            else:
                break
            i+=1

        return "".join(lst)
        
        