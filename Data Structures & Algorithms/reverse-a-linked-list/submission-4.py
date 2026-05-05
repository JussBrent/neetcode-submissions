# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            temp = curr.next #saves the rest of the list
            curr.next = prev #breaks the link
            prev = curr #stores the node for the link
            curr = temp #moves curr to working link
        return prev