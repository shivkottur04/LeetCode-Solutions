class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==i and nums[i]<10:
                return i
            if nums[i]>9:
                x=str(nums[i])
                lst=list(x)
                val=0
                for j in lst:
                    val+=int(j)
                if val==i:
                    return i
        return -1

                

        