# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        lst=[]
        temp=head
        while temp:
            lst.append(str(temp.val))
            temp=temp.next
        x="".join(lst)
        return int(x,2)

        