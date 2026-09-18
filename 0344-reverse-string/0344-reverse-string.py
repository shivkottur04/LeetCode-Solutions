class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)%2==0:
            i=0
            j=len(s)-1
            while i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        else:
            i=0
            j=len(s)-1
            while i<len(s)//2:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1