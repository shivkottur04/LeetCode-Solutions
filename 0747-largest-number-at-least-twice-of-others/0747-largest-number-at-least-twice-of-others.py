class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum=max(nums)
        flag=1
        x=0
        for i in range(len(nums)):
            if nums[i]==maximum:
                x=i
                pass
            else:
                if maximum >= 2*nums[i]:
                    pass
                else:
                    flag=0
                    break
        if flag==1:
            return x
        else:
            return -1

