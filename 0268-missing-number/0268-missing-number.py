class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        '''
        n=len(nums)
        total=(n*(n+1))/2
        arr_sum=sum(nums)
        return int(total-arr_sum)

