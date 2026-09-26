class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                lst.append(i)
        return lst
