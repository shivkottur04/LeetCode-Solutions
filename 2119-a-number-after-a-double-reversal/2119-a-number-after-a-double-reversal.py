class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev=list(str(num))
        rev.reverse()
        rev="".join(rev)
        rev=int(rev)
        rev=list(str(rev))
        rev.reverse()
        rev="".join(rev)
        rev=int(rev)
        if num==rev:
            return True
        else:
            return False

        
        