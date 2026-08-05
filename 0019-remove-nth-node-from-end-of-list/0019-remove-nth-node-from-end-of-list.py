# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            head=None
            return head
        else:
            temp1=head
            count=0
            while temp1:
                count+=1
                temp1=temp1.next
            #counts no. of steps to move forward
            x=count-n
            if x==0:
                return head.next
            temp2=head
            prev=None
            i=0
            while i<x:
                i+=1
                prev=temp2
                temp2=temp2.next
            prev.next=temp2.next
            return head

        