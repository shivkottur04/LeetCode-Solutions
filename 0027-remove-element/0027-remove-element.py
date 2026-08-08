class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                lst.append(nums[i])
        for i in range(len(lst)):
            nums[i]=lst[i]
        return len(lst)