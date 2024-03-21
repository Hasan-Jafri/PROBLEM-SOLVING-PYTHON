'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def reverseList(head):
    if not head or not head.next:
        return head
    else:
        prev = None
        current = head
        nextt = current.next
        while(nextt):
            prev = current
            current = nextt
            nextt = nextt.next
            current.next = prev
        current.next = prev 
        head.next = None
        return current

def display(head):
    curr = head
    while(curr):
        print(curr.val,end=' ')
        curr = curr.next
    print()

# Sample Input
head = ListNode(val=1)
head.next = ListNode(val=2)
head.next.next = ListNode(val=3)
head.next.next.next = ListNode(val=4)
head.next.next.next.next = ListNode(val=5)

display(head=head)
head = reverseList(head=head)
display(head=head)
    