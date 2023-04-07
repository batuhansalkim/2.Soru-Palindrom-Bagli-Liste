
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        N = 0
        while cur:
            N+=1
            cur = cur.next
        mid = N//2
        i = 0

        def reverse(head):
            ans = None
            while head:
                nx = head.next
                head.next = ans
                ans = head
                head = nx 
            return ans
        
        first = second = head
        while i<mid:
            second = second.next
            i+=1
        second = reverse(second)

        while first and second:
            if first.val != second.val: return False
            first = first.next
            second = second.next
        return True