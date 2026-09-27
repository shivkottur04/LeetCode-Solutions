class Solution:
    def averageValue(self, nums: list[int]) -> int:
        lst=[]
        for i in nums:
            if i%2==0 and i%3==0:
                lst.append(i)
        if lst:
            return int(sum(lst)/len(lst))
        else:
            return 0
        