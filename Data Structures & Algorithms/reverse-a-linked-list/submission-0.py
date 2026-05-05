# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None #initialize prev
        temp = head

        while temp: #while current node is null so it can reach the end
           
            next_node = temp.next #equals to 1; initialize
            temp.next = prev #moving node back
            prev = temp
            temp = next_node

        return prev
