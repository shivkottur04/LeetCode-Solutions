class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        s=[]
        for i in arr:
            if i != 0:
                s.append(i)
            else:
                s.append(i)
                s.append(0)
            if len(s)>=len(arr):
                break
        for i in range(len(s)):
            if i<len(arr):
                arr[i]=s[i]
            else:
                break

            