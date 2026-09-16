class Solution:
    def trimMean(self, arr: List[int]) -> float:
        five_percent=int(len(arr)*0.05)
        i=0
        while i<five_percent:
            arr.remove(min(arr))
            arr.remove(max(arr))
            i+=1
        return sum(arr)/len(arr)

        