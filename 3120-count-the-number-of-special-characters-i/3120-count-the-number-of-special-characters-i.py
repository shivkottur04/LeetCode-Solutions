class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=list(set(word))
        word.sort()
        count=0
        c=Counter(word)
        for i in word:
            if i.isupper():
                if i in c and i.lower() in c:
                    count+=1
            else:
                break
        return count
        