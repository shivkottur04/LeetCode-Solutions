class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        x=float('inf')
        for i in range(start,len(nums)):
            if nums[i]==target:
                x=i
                break
        y=float('inf')
        for i in range(start-1,-1,-1):
            if nums[i]==target:
                y=i
                break
        return min(abs(x-start),abs(y-start))
        
        