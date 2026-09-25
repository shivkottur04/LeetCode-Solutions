from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        d1=Counter(nums1)
        d2=Counter(nums2)
        for key in d1:
            lst.extend([key]*min(d1[key],d2[key]))
        return lst
        
        

         