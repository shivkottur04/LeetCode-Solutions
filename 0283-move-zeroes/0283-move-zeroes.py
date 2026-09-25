class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
                '''
        index=0
        for i in nums:
            if i != 0:
                nums[index]=i
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0
        return nums

        