'''
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    fast = slow = head
    # Finding Middle Node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reversing Middle Node
    prev = None
    curr = slow
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt

    middle_head = prev
    # Re-ordering lists
    start = head
    middle = middle_head
    while middle.next is not None:
        nextt = start.next
        nextt2 = middle.next
        start.next , middle.next = middle , start.next
        start = nextt
        middle = nextt2


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

display(head=head)
reorderList(head=head)
display(head=head)