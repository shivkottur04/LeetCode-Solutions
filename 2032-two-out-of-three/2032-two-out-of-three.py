class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        lst=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                lst.append(i)
        for i in nums2:
            if i in nums3:
                lst.append(i)
        return list(set(lst))
