# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # count the length of the linked list
        def getLenght(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        m = getLenght(headA)
        n = getLenght(headB)
        l1 = headA
        l2 = headB

        # make sure l1 is the longer list to make code easier
        if m < n:
            m, n = n, m
            l1, l2 = headB, headA
        
        # move the pointer of the longer list forward by the diference
        while m > n:
            l1 = l1.next
            m -= 1

        # move both pointers until the intersection is found
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1