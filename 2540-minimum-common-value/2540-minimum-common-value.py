class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1=set(nums1)
        nums2=set(nums2)
        num=nums1.intersection(nums2)
        if not num:
            return -1
        else:
            return min(num)
        