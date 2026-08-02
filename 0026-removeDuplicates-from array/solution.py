class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        unq=list(s)
        unq.sort()
        for i in range(len(unq)):
            nums[i]=unq[i]
        k=len(unq)
        return k
