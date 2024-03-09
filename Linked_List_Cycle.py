'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    # # Cheeky Logic with the help of constraint. As 10^4 is not big enough we can simply use this logic.
    # curr = head
    # size = 0
    # while(curr):
    #     curr = curr.next
    #     size += 1
    #     if size > 10**4:
    #         return True
    # return False

    # Hare and Tortoise Algorithm (Floyd's cycle Finding Algorithn)
    slow = fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Sample Input

head = ListNode(val=3)
head.next = ListNode(val=2)
head.next.next = ListNode(val=0)
head.next.next.next = ListNode(val=-4)
head.next.next.next.next = head.next

print(hasCycle(head = head))