class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=list(set(nums))
        if len(num)==1:
            return num[0]
        elif len(num)==2:
            num.sort()
            return num[1]
        else:
            n=len(num)-1
            num.sort()
            return num[n-2]