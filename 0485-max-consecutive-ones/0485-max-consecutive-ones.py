class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        lst=[]
        for i in nums:
            if i==1:
                maximum+=1
            else:
                lst.append(maximum)
                maximum=0
        lst.append(maximum)
        return max(lst)
            

        