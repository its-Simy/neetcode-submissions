# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        '''
        here i'm thinking a slow and fast pointer approach,

        bascially by trying and find 


        [1,2,3,4]
        s = 1
        f = 2

        s = 2
        f = 4

        s = 3
        f = 3
        if slow == fast
        return true, otherwise, return false


        set both to head

        and then move the faster item set to head.next.next

        while fast exists, we continue looping

        adn then jsut try to find when they're equal,

        if equal return true

        otherwise return true
        '''
        slow = head
        if not head or not head.next or not head.next.next:
            return False
        fast = head.next.next
        
        while fast: 
            if fast == slow:
                return True
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
        
        return False