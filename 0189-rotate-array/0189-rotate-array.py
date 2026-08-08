class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        while i<k:
            x=nums.pop()
            nums.insert(0,x)
            i+=1
        