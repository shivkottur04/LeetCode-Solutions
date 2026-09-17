class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        lst=[]
        words.sort(key=len)
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    lst.append(words[i])
                    break
        return lst