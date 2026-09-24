from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        ans=""
        for key,val in d.items():
            ans+=key*val
        return ans
        
        
        