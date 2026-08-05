class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        lst=[]
        while nums:
            x=min(nums)
            y=max(nums)
            average=(x+y)/2
            nums.remove(x)
            nums.remove(y)
            lst.append(average)
        return min(lst)

        