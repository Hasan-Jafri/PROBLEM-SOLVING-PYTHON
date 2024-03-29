'''
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.


(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_Sum_Node = {}
    preSum = 0
    current = dummy
    while current:
        preSum += current.val
        if preSum in prefix_Sum_Node:
            previous_Node = prefix_Sum_Node[preSum]
            to_remove = previous_Node.next
            removal_Sum = preSum + (to_remove.val if to_remove else 0)
            while removal_Sum != preSum:
                del prefix_Sum_Node[removal_Sum]
                to_remove = to_remove.next
                removal_Sum += to_remove.val if to_remove else 0
            previous_Node.next = current.next
        else:
            prefix_Sum_Node[preSum] = current
        current = current.next

    return dummy.next

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
head.next.next.next = ListNode(val=-3)
head.next.next.next.next = ListNode(val=-2)
n = 2
display(head)
ans = removeZeroSumSublists(head=head)
display(ans)