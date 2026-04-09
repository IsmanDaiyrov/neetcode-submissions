# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            return prev

        l1 = reverseLinkedList(l1)
        l2 = reverseLinkedList(l2)

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            new_num = num1 + num2 + carry
            carry = new_num // 10
            new_num = new_num % 10

            curr.next = ListNode(new_num)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return reverseLinkedList(dummy.next)