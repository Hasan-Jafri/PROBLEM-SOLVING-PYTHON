'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 
Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getsize(head)->int:
    curr = head
    size = 0
    while(curr):
        curr = curr.next
        size += 1
    return size
def middleNode(head):
    size = getsize(head)
    middle = int(size/2) + 1
    curr = head
    while(middle != 1):
        curr = curr.next
        middle -= 1
    return curr

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

display(head)
head = middleNode(head=head)
display(head)