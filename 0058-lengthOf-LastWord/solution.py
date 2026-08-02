class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=s.split()
        n=len(lst)
        return len(lst[n-1])
