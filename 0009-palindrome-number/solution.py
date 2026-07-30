class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        org=x
        x=str(x)
        rev=x[::-1]
        rev=int(rev)
        if org==rev:
            return True
        else:
            return False
