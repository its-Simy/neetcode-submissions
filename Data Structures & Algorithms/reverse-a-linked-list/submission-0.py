# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, current):
        if head == None:
            return current
        
        temp = head.next
        head.next = current
        current = head
        head = temp
        return self.reverse(head,current)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head,None)
    
   