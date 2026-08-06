class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        lst=[]
        for i in nums1:
            n=len(lst)
            x=nums2.index(i)
            for j in range(x+1,len(nums2)):
                if nums2[j]>nums2[x]:
                    lst.append(nums2[j])
                    break
            if not lst:
                lst.append(-1)
            elif len(lst) == n:
                lst.append(-1)
        return lst
        