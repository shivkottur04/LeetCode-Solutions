class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count=0
        words=set(words1)
        for i in words:
            if i in words2 and words1.count(i)==1 and words2.count(i)==1:
                count+=1
        return count
        