class Solution:
    def reverseVowels(self, s: str) -> str:
        lst=list(s)
        index=[]
        vowels=[]
        for i in range(len(lst)):
            if lst[i].lower() in "aeiou":
                index.append(i)
                vowels.append(lst[i])
        index.reverse()
        for i in range(len(index)):
            lst[index[i]]=vowels[i]
        return "".join(lst)