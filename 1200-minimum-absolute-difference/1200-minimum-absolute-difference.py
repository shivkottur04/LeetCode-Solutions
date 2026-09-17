class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        smallest=float('inf')
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<smallest:
                smallest=abs(arr[i]-arr[i+1])
        lst=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==smallest:
                lst.append([arr[i],arr[i+1]])
        
        return lst

