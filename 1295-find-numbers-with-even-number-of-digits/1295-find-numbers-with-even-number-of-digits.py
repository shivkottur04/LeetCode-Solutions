class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        
        for i in nums:
            lst=[]
            i=str(i)
            lst=list(i)
            n=len(lst)
            if n%2==0:
                count+=1
            else:
                pass
        return count
        