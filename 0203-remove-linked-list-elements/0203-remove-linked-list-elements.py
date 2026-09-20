# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        temp=head
        prev=None
        while temp:
            if temp.val==val:
                if temp==head:
                    head=head.next
                    temp=head
                else:
                    temp=temp.next
                    prev.next=temp
            else:
                prev=temp
                temp=temp.next
        return head

            

        