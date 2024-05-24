'''
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root,is_left: bool)->int:
    if not root:
        return 0
    if not root.left and not root.right:
        if is_left:
            return root.val
        else:
            return 0
    left_sum = dfs(root.left,True)
    right_sum = dfs(root.right,False)
    return left_sum + right_sum
def sumOfLeftLeaves(root) -> int:
    
    return dfs(root,False)


root = TreeNode(val = 3)
root.left = TreeNode(val = 9)
root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

print(sumOfLeftLeaves(root=root))