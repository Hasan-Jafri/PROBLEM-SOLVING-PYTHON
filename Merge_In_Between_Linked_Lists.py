'''
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

 

Example 1:


Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1, a, b, list2):
    i = j = 0
    # For location a.
    a_node = list1
    while(i < a):
        a_node = a_node.next
        i += 1
    # For location b
    b_node = list1
    while(j < b):
        b_node = b_node.next
        j += 1
    
    list2_end = list2
    while(list2_end.next):
        list2_end = list2_end.next
    
    # Condition if a == b
    if a_node == b_node:
        list2_end.next = a_node.next
        a_node.val = list2.val
        a_node.next = list2.next
        
    else:
        a_node.val = list2.val
        a_node.next = list2.next
        list2_end.next = b_node.next
    

    return list1

def display(head):
    curr = head
    while(curr):
        print(curr.val,end=' ')
        curr = curr.next
    print()

# Sample Input
list1 = ListNode(val=10)
list1.next = ListNode(val=1)
list1.next.next = ListNode(val=13)
list1.next.next.next = ListNode(val=6)
list1.next.next.next.next = ListNode(val=9)
list1.next.next.next.next.next = ListNode(val=5)

display(head=list1)

list2 = ListNode(val=1000000)
list2.next = ListNode(val=1000001)
list2.next.next = ListNode(val=1000002)

display(head=list2)

a = 3
b = 4

head = mergeInBetween(list1=list1,list2=list2,a=a,b=b)
display(head=head)

