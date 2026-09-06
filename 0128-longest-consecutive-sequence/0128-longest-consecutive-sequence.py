class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        lst=[]
        count=1
        for i in range(len(nums)-1):   
            if nums[i+1]==nums[i]+1:
                count+=1
            else:
                lst.append(count)
                count=1
        lst.append(count)
        return max(lst)

            
        