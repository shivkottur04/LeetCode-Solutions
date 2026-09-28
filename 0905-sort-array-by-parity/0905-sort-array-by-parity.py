class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
            if len(nums)==0 or len(nums)==1:
                return nums
            lst1=[]
            lst2=[]
            for i in nums:
                if i%2==0:
                    lst1.append(i)
                else:
                    lst2.append(i)
            lst1.extend(lst2)
            return lst1