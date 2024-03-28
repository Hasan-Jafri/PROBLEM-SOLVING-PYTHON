'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # O(n) Time, O(n) Space
    '''
    result = ''
    curr = head
    while(curr):
        result += str(curr.val)
        curr = curr.next
    return result == result[::-1]
    '''

    # O(n) Time, O(1) Space

    if not head or not head.next:
        return True
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

    # To check for palindrome.
    start = head
    middle = middle_head
    while middle:
        if start.val != middle.val:
            return False
        start = start.next
        middle = middle.next
    return True

# Sample Input
head = ListNode(val=1)
head.next = ListNode(val=2)
head.next.next = ListNode(val=2)
head.next.next.next = ListNode(val=1)

print(isPalindrome(head=head))