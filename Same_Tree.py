'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q) -> bool:
    null_p = p is None
    null_q = q is None

    if null_p and null_q:
        return True
    elif null_p or null_q:
        return False
    else:
        status = p.val == q.val
        status = status and isSameTree(p.right,q.right)
        status = status and isSameTree(p.left,q.left)
        return status
    
# Sample Input
p = TreeNode(val = 1)
q = TreeNode(val = 1)
p.left = TreeNode(val = 2)
p.right = TreeNode(val = 3)
q.left = TreeNode(val = 2)
q.right = TreeNode(val = 3)

print(isSameTree(p,q))