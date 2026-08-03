class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number="".join(map(str,digits))
        num=int(number)
        num=num+1
        digits=list(map(int,str(num)))
        return digits
