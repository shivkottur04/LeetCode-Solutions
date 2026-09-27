class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        count=0
        for i in nums1:
            if i in nums2:
                count+=1
        lst.append(count)
        count=0
        for i in nums2:
            if i in nums1:
                count+=1
        lst.append(count)
        return lst
        