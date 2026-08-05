class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sums=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                sums+=nums[i]**2
        return sums
        