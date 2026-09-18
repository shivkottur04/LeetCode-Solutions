class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in nums:
            i=str(i)
            for j in i:
                lst.append(int(j))
        
        return lst


        