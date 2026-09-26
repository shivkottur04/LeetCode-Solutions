class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=int(len(s)//2)
        a=s[0:n]
        b=s[n:len(s)]
        vowels=[0]*2
        consonents=[0]*2
        for i in a:
            if i.lower() in "aeiou":
                vowels[0]+=1
            else:
                consonents[0]+1
        for i in b:
            if i.lower() in "aeiou":
                vowels[1]+=1
            else:
                consonents[1]+1
        if vowels[0]==vowels[1] and consonents[0]==consonents[1]:
            return True
        else:
            return False
        