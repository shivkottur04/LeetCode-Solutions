class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        lst=[]
        for i in range(1,max(arr)+k+1):
            if i not in arr:
                lst.append(i)
        return lst[k-1]
        