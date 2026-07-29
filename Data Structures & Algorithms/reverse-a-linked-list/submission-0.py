# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        l=head
        a=[]
        while(head!=None):
            a.append(head.val)
            head=head.next
        head=l
        for i in range(len(a)-1,-1,-1):
            head.val=a[i]
            head=head.next
        return l

