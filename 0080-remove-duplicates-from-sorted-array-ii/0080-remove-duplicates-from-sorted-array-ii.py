class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        lst=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]<=2:
                lst.append(i)
        for i in range(len(lst)):
            nums[i]=lst[i]

                
        return len(lst)
        

        
        