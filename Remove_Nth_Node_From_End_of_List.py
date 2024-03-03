'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getSize(head):
    size = 0
    curr = head
    while(curr):
        curr = curr.next
        size += 1
    return size
def removeNthFromEnd(head, n):
    size = getSize(head)
    if size == 0 or n > size:
        return head
    elif n == size:
        head = head.next
    else:
        curr = head
        prev = None
        while(size != n):
            prev = curr
            curr = curr.next
            size -= 1
        prev.next = curr.next
        curr.next = None
    return head

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
n = 2
display(head)
ans = removeNthFromEnd(head=head,n=n)
display(ans)