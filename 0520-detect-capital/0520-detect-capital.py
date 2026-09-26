class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper=0
        for i in word:
            if i.isupper():
                upper+=1
        if upper==len(word) or upper==0 or (upper==1 and word[0].isupper()):
            return True
        else:
            return False
        