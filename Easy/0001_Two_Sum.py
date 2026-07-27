class Solution:
    def twosum(self,a,target):
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]+a[j]==target:
                    lst=[i,j]
                    return lst
s=Solution()                    
arr=list(map(int,input()))
target=int(input())
print(s.twosum(arr,target))
 
