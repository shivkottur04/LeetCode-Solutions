class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for i in s:
            if i.isalnum():
                x=i.lower()
                lst.append(x)
        if lst==lst[::-1]:
            return True
        else:
            return False
