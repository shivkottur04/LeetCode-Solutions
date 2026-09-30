class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst=[]
        for i in nums:
            if i>0:
                lst.append(i)
        lst=list(set(lst))
        lst.sort()
        for i in range(len(lst)):
            if lst[i] != i+1:
                return i+1
        return len(lst)+1

                

        