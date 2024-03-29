'''
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def getsize(head) -> int:
    size = 0
    curr = head
    while(curr):
        curr = curr.next
        size += 1
    return size
def deleteMiddle(head):
    size = getsize(head)
    if size == 0:
        return head
    elif size == 1:
        head = head.next
    else:
        middle = int(size/2) + 1
        curr = head
        prev = None
        while(middle != 1):
            prev = curr
            curr = curr.next
            middle -= 1
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
head.next = ListNode(val=3)
head.next.next = ListNode(val=4)
head.next.next.next = ListNode(val=7)
head.next.next.next.next = ListNode(val=1)
head.next.next.next.next.next = ListNode(val=2)
head.next.next.next.next.next.next = ListNode(val=6)

display(head=head)
head = deleteMiddle(head=head)
display(head=head)