class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        i=0
        
        lst=[]
        while i<len(chars):
            j=i+1
            count=1
            while j<len(chars) and chars[i]==chars[j]:
                count+=1
                j+=1
            lst.append(chars[i])
            
            if count>1 and count<10:
                lst.append(str(count))
            if count>9:
                count=str(count)
                a=list(count)
                lst.extend(a)
            i=j
        chars.clear()
        chars.extend(lst)
        return len(chars)
        
            

        