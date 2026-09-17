class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        d={}
        for i in range(left,right+1):
            d[i]=0
        for i in range(left,right+1):
            for j in range(len(ranges)):
                if i in range(ranges[j][0],ranges[j][1]+1):
                    d[i]=1
                    break
        for key in d.keys():
            if d[key]==0:
                return False
        return True
                    

        