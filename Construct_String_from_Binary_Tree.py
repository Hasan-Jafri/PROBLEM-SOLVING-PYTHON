'''
606. Construct String from Binary Tree


Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree
with the preorder traversal way, and return it.Omit all the empty parenthesis pairs that do not affect the 
one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:

Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree():
    root_value = int(input("Enter Root Value: "))
    root = TreeNode(root_value)

    queue = [root]

    while queue:
        current = queue.pop(0)

        left_value = int(input(f"Enter Left Child of {current.val} (Enter -1 if none): "))
        if left_value != -1:
            left_child = TreeNode(left_value)
            current.left = left_child
            queue.append(left_child)

        right_value = int(input(f"Enter Right Child of {current.val} (Enter -1 if none): "))
        if right_value != -1:
            right_child = TreeNode(right_value)
            current.right = right_child
            queue.append(right_child)

    return root

def preOrderTraversal(root, result):
    if root is None:
        return 
    result.append(str(root.val))
    if root.left is not None or root.right is not None:
        result.append("(")
        preOrderTraversal(root.left,result)
        result.append(")")
    if root.right is not None:
        result.append("(")
        preOrderTraversal(root.right,result)
        result.append(")")

def tree2str(root):
    if root is None:
        return ""

    result = []
    preOrderTraversal(root,result)
    return ''.join(result)

root = build_binary_tree()
print(tree2str(root=root))
