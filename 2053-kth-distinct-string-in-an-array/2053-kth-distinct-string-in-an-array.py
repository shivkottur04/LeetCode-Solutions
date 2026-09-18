class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        lst=[]
        for i in range(len(arr)):
            if i==0:
                if arr[i] not in arr[i+1:len(arr)+1]:
                    lst.append(arr[i])
            elif i==len(arr)-1:
                if arr[i] not in arr[i-1::-1]:
                    lst.append(arr[i])
            else:
                if arr[i] not in arr[i+1:len(arr)+1] and arr[i] not in arr[i-1::-1]:
                    lst.append(arr[i])
        if k<=len(lst):
            return lst[k-1]
        else:
            return ""
        