class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''s=set(nums)
        unq=list(s)
        unq.sort()
        for i in range(len(unq)):
            nums[i]=unq[i]
        k=len(unq)
        return k'''

        #method 2
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1

            