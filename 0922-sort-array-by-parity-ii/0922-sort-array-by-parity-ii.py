class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd=[]
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even.pop(0)
            else:
                nums[i]=odd.pop(0)
        return nums
        