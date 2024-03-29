'''
513. Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


def findBottomLeftValue(root) -> int:
    queue = deque()
    left_most = None
    queue.append(root)
    while queue:
        root = queue.popleft()
        left_most = root.val
        if root.right:
            queue.append(root.right)
        if root.left:
            queue.append(root.left)
    return left_most

# Sample Input
root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.left.left = TreeNode(val=4)
root.right.left = TreeNode(val=5)
root.right.right = TreeNode(val=6)
root.right.left.left = TreeNode(val=7)

print(findBottomLeftValue(root = root))