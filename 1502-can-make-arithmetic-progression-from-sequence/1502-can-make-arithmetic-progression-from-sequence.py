class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        lst=[]
        for i in range(len(arr)-1):
            lst.append(arr[i]-arr[i+1])
        if len(set(lst))==1:
            return True
        else:
            return False
        