class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count=0
        for i in sentences:
            lst=i.split()
            if len(lst)>count:
                count=len(lst)
        return count
        