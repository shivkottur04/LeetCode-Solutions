class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=strs[0]
        b=strs[-1]
        i=0
        j=0
        lst=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                lst.append(a[i])
            else:
                break
            i+=1
            j+=1
        return "".join(lst)
        
        