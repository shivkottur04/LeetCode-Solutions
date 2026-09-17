class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        lst=[]
        while i<len(nums)//2:
            lst.append(nums[i])
            lst.append(nums[i+n])
            i+=1
        return lst
