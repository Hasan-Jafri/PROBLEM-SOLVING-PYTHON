'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root, diameter):
    if not root: # Edge case where the node is empty.
        return 0
    left = height(root.left,diameter) # For left height
    right = height(root.right,diameter) # For right height
    diameter[0] = max(diameter[0],left+right) # In each recursive call the diameter value is getting updated. It is passed as a list due to modification.
    return max(left,right) + 1 # After updating the diameter we make sure the height is retained so we return max of left and right height.

def diameterOfBinaryTree(root):
    diameter = [0] # Created a list to store the results as variables were not getting updated.
    height(root,diameter)
    return diameter[0]

# Sample Input
root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.left.left = TreeNode(val=4)
root.left.right = TreeNode(val=5)

print(diameterOfBinaryTree(root = root))